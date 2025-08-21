"""Simple teachable Notion-like CLI for notes, saved to JSON and exportable to Markdown.

Features:
- Create pages, add blocks (text, todo, code), list and view pages.
- Save/load data to `notion_data.json` (in the same folder).
- Export a page to Markdown.
- `--demo` mode builds sample pages and prints an export.

This file is intentionally compact and heavily commented for use in a short
YouTube walkthrough covering classes, file I/O, CLI with argparse, and simple
serialization.
"""

from __future__ import annotations

import argparse
import json
import os
import textwrap
from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import List, Dict, Any


DATA_FILE = os.path.join(os.path.dirname(__file__), "notion_data.json")


@dataclass
class Block:
	"""A block is a unit of content on a page: plain text, todo, or code."""

	type: str  # 'text', 'todo', or 'code'
	content: str
	checked: bool = False  # only used for todo
	language: str = ""  # only used for code blocks

	def to_dict(self) -> Dict[str, Any]:
		return asdict(self)


@dataclass
class Page:
	id: str
	title: str
	created_at: str
	blocks: List[Block] = field(default_factory=list)

	def to_dict(self) -> Dict[str, Any]:
		return {
			"id": self.id,
			"title": self.title,
			"created_at": self.created_at,
			"blocks": [b.to_dict() for b in self.blocks],
		}


class NotionLite:
	"""Minimal Notion-like manager: load/save pages and export to Markdown."""

	def __init__(self, data_file: str = DATA_FILE):
		self.data_file = data_file
		self.pages: Dict[str, Page] = {}
		self._load()

	# Persistence
	def _load(self):
		if not os.path.exists(self.data_file):
			self.pages = {}
			return
		try:
			with open(self.data_file, "r", encoding="utf-8") as f:
				raw = json.load(f)
		except Exception:
			# If file is corrupted, start fresh but keep the filename
			print("Warning: couldn't read data file — starting with empty DB")
			self.pages = {}
			return

		for pid, pdata in raw.items():
			blocks = [Block(**b) for b in pdata.get("blocks", [])]
			page = Page(id=pid, title=pdata["title"], created_at=pdata["created_at"], blocks=blocks)
			self.pages[pid] = page

	def _save(self):
		serial = {pid: p.to_dict() for pid, p in self.pages.items()}
		with open(self.data_file, "w", encoding="utf-8") as f:
			json.dump(serial, f, indent=2, ensure_ascii=False)

	# Basic operations
	def create_page(self, title: str) -> Page:
		pid = title.lower().replace(" ", "-")[:40]
		if pid in self.pages:
			# make unique
			pid = f"{pid}-{len(self.pages) + 1}"
		page = Page(id=pid, title=title, created_at=datetime.utcnow().isoformat())
		self.pages[pid] = page
		self._save()
		return page

	def add_block(self, page_id: str, block: Block) -> None:
		page = self.pages.get(page_id)
		if not page:
			raise KeyError(f"No page with id {page_id}")
		page.blocks.append(block)
		self._save()

	def list_pages(self) -> List[Page]:
		return list(self.pages.values())

	def get_page(self, page_id: str) -> Page:
		page = self.pages.get(page_id)
		if not page:
			raise KeyError(f"No page with id {page_id}")
		return page

	# Export helpers
	def page_to_markdown(self, page: Page) -> str:
		lines: List[str] = [f"# {page.title}", f"_Created: {page.created_at}_", ""]
		for b in page.blocks:
			if b.type == "text":
				lines.append(b.content)
				lines.append("")
			elif b.type == "todo":
				mark = "x" if b.checked else " "
				lines.append(f"- [{mark}] {b.content}")
			elif b.type == "code":
				lang = b.language or ""
				lines.append(f"```{lang}")
				lines.append(b.content)
				lines.append("```")
				lines.append("")
			else:
				lines.append(f"<!-- unknown block type: {b.type} -->")
		return "\n".join(lines)


def build_demo(n: NotionLite):
	"""Create a small demo dataset and return one exported page as string."""
	p = n.create_page("Python Tips")
	n.add_block(p.id, Block(type="text", content="A few handy Python tips for your next video."))
	n.add_block(p.id, Block(type="todo", content="Record intro", checked=False))
	n.add_block(p.id, Block(type="todo", content="Show examples", checked=True))
	code = textwrap.dedent(
		"""
		def greet(name):
			return f"Hello, {name}!"

		print(greet('YouTube'))
		"""
	).strip()
	n.add_block(p.id, Block(type="code", content=code, language="python"))
	return n.page_to_markdown(p)


def main(argv=None):
	parser = argparse.ArgumentParser(description="Tiny Notion-like CLI (teaching example)")
	sub = parser.add_subparsers(dest="cmd")

	sub.add_parser("list", help="List pages")

	create = sub.add_parser("create", help="Create a new page")
	create.add_argument("title")

	view = sub.add_parser("view", help="View page (markdown) by id")
	view.add_argument("id")

	add = sub.add_parser("add-text", help="Add a text block")
	add.add_argument("id")
	add.add_argument("content")

	todo = sub.add_parser("add-todo", help="Add a todo block")
	todo.add_argument("id")
	todo.add_argument("content")
	todo.add_argument("--checked", action="store_true")

	code = sub.add_parser("add-code", help="Add a code block")
	code.add_argument("id")
	code.add_argument("file", help="Path to a file to load as code")
	code.add_argument("--lang", default="", help="Language for fenced code block")

	export = sub.add_parser("export", help="Export page to markdown")
	export.add_argument("id")

	parser.add_argument("--demo", action="store_true", help="Create demo pages and print a sample export")

	args = parser.parse_args(argv)

	n = NotionLite()

	# Demo mode: quick showcase for recordings
	if args.demo:
		md = build_demo(n)
		print(md)
		return

	if args.cmd == "list":
		pages = n.list_pages()
		if not pages:
			print("(no pages yet)")
			return
		for p in pages:
			print(f"{p.id}: {p.title} ({len(p.blocks)} blocks)")

	elif args.cmd == "create":
		p = n.create_page(args.title)
		print(f"Created page: {p.id} - {p.title}")

	elif args.cmd == "view":
		try:
			p = n.get_page(args.id)
		except KeyError as e:
			print(e)
			return
		print(n.page_to_markdown(p))

	elif args.cmd == "add-text":
		try:
			n.add_block(args.id, Block(type="text", content=args.content))
			print("Added text block")
		except KeyError as e:
			print(e)

	elif args.cmd == "add-todo":
		try:
			n.add_block(args.id, Block(type="todo", content=args.content, checked=args.checked))
			print("Added todo block")
		except KeyError as e:
			print(e)

	elif args.cmd == "add-code":
		if not os.path.exists(args.file):
			print("Code file not found")
			return
		with open(args.file, "r", encoding="utf-8") as f:
			src = f.read()
		try:
			n.add_block(args.id, Block(type="code", content=src, language=args.lang))
			print("Added code block")
		except KeyError as e:
			print(e)

	elif args.cmd == "export":
		try:
			p = n.get_page(args.id)
		except KeyError as e:
			print(e)
			return
		print(n.page_to_markdown(p))

	else:
		parser.print_help()


if __name__ == "__main__":
	main()

