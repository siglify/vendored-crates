# Vendored crates

Copies of other projects' Rust crates that [siglify-app](https://github.com/siglify/siglify-app) builds with Siglify's and Herdr's patches, and `ghostty-sys`, its bindings to Ghostty. siglify-app uses them as git dependencies pinned to a commit of this repository, so every checkout builds them the same way.

| Folder | Origin | License |
| -- | -- | -- |
| `vendor/gpui-pre`, `gpui-pre-apple`, `gpui-pre-linux`, `gpui-pre-macos`, `gpui-pre-wgpu`, `gpui-pre-windows` | the `gpui-pre` crates on crates.io | Apache-2.0 (`LICENSE-APACHE` in each) |
| `vendor/gpui-kit` | [longbridge/gpui-kit](https://github.com/longbridge/gpui-kit) | Apache-2.0 (`LICENSE-APACHE`) |
| `vendor/quickjs-jit-runtime` | [longbridge/quickjs-jit](https://github.com/longbridge/quickjs-jit), its `jit/` crate | MIT (`LICENSE`) |
| `vendor/zed-xim`, `vendor/xim-ctext` | the `zed-xim` and `xim-ctext` crates on crates.io | MIT (`LICENSE` in each) |
| `vendor/ghostty` | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty), unmodified, as a git submodule | MIT (`LICENSE`) |
| `crates/ghostty-sys` | [Herdr](https://github.com/herdrdev/herdr-app) | Apache-2.0 (`LICENSE`) |

Herdr vendored these crates first; this repository continues from Herdr's copies, with their history.

## Changed files

A file Siglify changed carries this line at the top, as Apache-2.0 section 4(b) requires:

```
Modified by Siglify, Inc. Copyright (c) 2026 Siglify, Inc. for modifications.
```

The history keeps the line between authors: commits with a `Herdr-Release:` or `Upstream-Release:` trailer hold other people's code (the crates as released, Herdr's changes, a newer release Siglify moved to), and the commits after them Siglify's. `scripts/check-notices.py` checks on every push to `master` that each file differing from the latest of those carries the line.

## Changing a crate

To move a crate to a newer release, commit the release unchanged first, with an `Upstream-Release:` trailer, then our changes on top. Commit here, then set the new commit as the `rev` of these dependencies in siglify-app's `Cargo.toml`.
