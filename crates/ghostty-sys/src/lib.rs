// Modified by Siglify, Inc. Copyright (c) 2026 Siglify, Inc. for modifications.
#![allow(non_camel_case_types, non_snake_case, non_upper_case_globals, dead_code, clippy::all)]

include!(concat!(env!("OUT_DIR"), "/bindings.rs"));

/// Files of vendor/ghostty that siglify-app embeds.
pub const NOTO_EMOJI: &[u8] = include_bytes!("../../../vendor/ghostty/src/font/res/NotoEmoji-Regular.ttf");
pub const KITTY_GRAPHICS_UNICODE: &str = include_str!("../../../vendor/ghostty/src/terminal/kitty/graphics_unicode.zig");
