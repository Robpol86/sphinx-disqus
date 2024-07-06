# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- N/A

## [1.3.0] - 2024-07-06

### Added

- Python 3.10 through 3.12 support

### Removed

- Dropped Python 3.6 and 3.7 support due to EOL
- Dropped Python 3.8 support for latest Sphinx compatibility

### Changed

- No longer depending on jQuery for delayed loading of embed.js ([#33](https://github.com/Robpol86/sphinx-disqus/pull/33))
- Now supporting Sphinx themes that don't use jQuery

## [1.2.0] - 2021-06-10

### Added

- Support for `file://` ([#15](https://github.com/Robpol86/sphinx-disqus/pull/15))

### Removed

- Dropped Python 2.7 and <3.6 support

### Fixed

- Support for Sphinx 1.6+ ([#7](https://github.com/Robpol86/sphinx-disqus/pull/7))
- Fixed new html_static_path append and timing ([#15](https://github.com/Robpol86/sphinx-disqus/pull/15))

### Changed

- Re-licensed from MIT to BSD 2-Clause
- Renamed project from `sphinxcontrib-disqus` to `sphinx-disqus`
- Updated disqus.js with their latest universal code

## [1.1.0] - 2016-08-04

### Added

- Python 3.5 support (Linux/OS X and Windows).

### Fixed

- easy_install: https://bitbucket.org/birkenfeld/sphinx-contrib/issues/155/
- https://github.com/Robpol86/sphinxcontrib-disqus/issues/2
- https://github.com/Robpol86/sphinxcontrib-disqus/issues/1
- https://github.com/Robpol86/sphinxcontrib-disqus/issues/3

## [1.0.0] - 2015-07-31

### Added

- Initial release.
