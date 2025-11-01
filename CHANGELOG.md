# Changelog

## 1.0.0-alpha.12 (2025-11-01)

Full Changelog: [v1.0.0-alpha.11...v1.0.0-alpha.12](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.11...v1.0.0-alpha.12)

### Features

* add error handle to stainless stream response ([318c45c](https://github.com/letta-ai/letta-python/commit/318c45c319d0cf5a044384e0d78cf40fbc253ae0))
* add project and project_id fields to stainless client ([ecdf72d](https://github.com/letta-ai/letta-python/commit/ecdf72d35a160657cb8905b784c0de7ccf45f875))
* provider-specific model configuration ([3ed0b5e](https://github.com/letta-ai/letta-python/commit/3ed0b5eda4029333f0c4698414418c5ebac369c2))
* Revert "feat: provider-specific model configuration " ([60a6788](https://github.com/letta-ai/letta-python/commit/60a6788de725c8dcbbb8fe19f26787dc2e063351))


### Bug Fixes

* **client:** close streams without requiring full consumption ([c5cf389](https://github.com/letta-ai/letta-python/commit/c5cf3892a1268bee165cf1be12f58785457cf368))
* stainless merge build dependency on changed files ([8d58345](https://github.com/letta-ai/letta-python/commit/8d583458fa477095b933d53d5159d35cf533575d))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([52b9651](https://github.com/letta-ai/letta-python/commit/52b9651366c3362b2a02f3303ff363bc6492cbce))
* verify stainless merge build ([c0ec157](https://github.com/letta-ai/letta-python/commit/c0ec157b0ffb3bea919f6e32f895f7f34e1d195d))

## 1.0.0-alpha.11 (2025-10-29)

Full Changelog: [v1.0.0-alpha.10...v1.0.0-alpha.11](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.10...v1.0.0-alpha.11)

### Features

* add streaming response type to messages stream for stainless ([1312c59](https://github.com/letta-ai/letta-python/commit/1312c59d19bd36d5bff27a6dc968d77bb1f5d7e8))


### Bug Fixes

* toggle off stainless pagination for list endpoints that require id field ([23d68c8](https://github.com/letta-ai/letta-python/commit/23d68c8198c0394f27df77524f4f1810e49a234d))
* use api base url for cloud ([1c44e39](https://github.com/letta-ai/letta-python/commit/1c44e39a62290d7fb01d1c2f6758952dc374a960))
* use api base url for cloud ([406ae87](https://github.com/letta-ai/letta-python/commit/406ae8714589f356e16500aa4b7e661bc35c99f7))

## 1.0.0-alpha.10 (2025-10-24)

Full Changelog: [v1.0.0-alpha.9...v1.0.0-alpha.10](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.9...v1.0.0-alpha.10)

### Features

* clean up block return object  [LET-5784] ([28e4290](https://github.com/letta-ai/letta-python/commit/28e429013837a18d39645183df6f87bb76df5510))


### Chores

* rename update methods to modify in stainless ([6be374c](https://github.com/letta-ai/letta-python/commit/6be374cdeebb3c89497be7e28544b2bb165941b8))

## 1.0.0-alpha.9 (2025-10-24)

Full Changelog: [v1.0.0-alpha.8...v1.0.0-alpha.9](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.8...v1.0.0-alpha.9)

### Features

* add pagination config for list agent files ([a95c0df](https://github.com/letta-ai/letta-python/commit/a95c0df84af6edc5274a1adf62b528e86bfeda50))
* add pagination configuration for list batch message endpoint ([d5a8165](https://github.com/letta-ai/letta-python/commit/d5a8165da29148a9579b01bc8ada35eb50160186))
* make some routes return none for sdk v1 ([2c71c46](https://github.com/letta-ai/letta-python/commit/2c71c468ce408bfe19514dd3d2cb34ca440450b1))


### Chores

* add order_by param to list archives [LET-5839] ([bc4b1c8](https://github.com/letta-ai/letta-python/commit/bc4b1c8a6ab51b30f6bdc48995c4cc29921475e6))

## 1.0.0-alpha.8 (2025-10-24)

Full Changelog: [v1.0.0-alpha.7...v1.0.0-alpha.8](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.7...v1.0.0-alpha.8)

### Features

* add stainless pagination for identities ([65eef2e](https://github.com/letta-ai/letta-python/commit/65eef2eab1c234a8146bcd2bec28e184a4626872))

## 1.0.0-alpha.7 (2025-10-24)

Full Changelog: [v1.0.0-alpha.6...v1.0.0-alpha.7](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.6...v1.0.0-alpha.7)

### Features

* add agent template route to config ([8eeda3f](https://github.com/letta-ai/letta-python/commit/8eeda3f8e946eced4fe1a0dfb7798d748aabb8fc))
* add new archive routes to sdk ([2b0a253](https://github.com/letta-ai/letta-python/commit/2b0a2536cd5c14d5dcf2770c79aabcab426642c4))
* add openai-style include param for agents relationship loading ([acb797b](https://github.com/letta-ai/letta-python/commit/acb797bb966dc05ca59fef4fcec3b2b2bed83580))
* deprecate append copy suffix, add override name [LET-5779] ([1b51b08](https://github.com/letta-ai/letta-python/commit/1b51b082a92e9183789e0fabe3838b4e75312a28))
* fix patch approvals endpoint incorrectly using queyr params ([d6a4fe6](https://github.com/letta-ai/letta-python/commit/d6a4fe6a48cd93d891cc635f356f85a1ff199a4a))
* remove run tool for external sdk ([3c1b717](https://github.com/letta-ai/letta-python/commit/3c1b71780b5baecda6e246f8c1d034d62adcecc2))
* remove unused max length parameter ([85b5f00](https://github.com/letta-ai/letta-python/commit/85b5f00fcbb7d825dfdc7065f867600b718863b7))
* rename multi agent group to managed group ([733e959](https://github.com/letta-ai/letta-python/commit/733e959a5951d080a5c7318c5a98d724c18d86ef))
* replace agent.identity_ids with agent.identities ([900384e](https://github.com/letta-ai/letta-python/commit/900384e2d4a73a9a2dae9076182e19902daa77b7))
* reset message incorrectly using query param ([06229f4](https://github.com/letta-ai/letta-python/commit/06229f43eaaffdf5a2b355e28f550abc7540c65f))
* Revert "feat: revise mcp tool routes [LET-4321]" ([a77127e](https://github.com/letta-ai/letta-python/commit/a77127eb90b3e79264cf7cd6b12a70859393c9d7))
* Support embedding config on the archive [LET-5832] ([ccfc935](https://github.com/letta-ai/letta-python/commit/ccfc935d425c24a782bdda272a39defd012b9bfa))


### Bug Fixes

* sdk config code gen ([6074e64](https://github.com/letta-ai/letta-python/commit/6074e6480ad03e057639b40f983029ae01d9f7d1))


### Chores

* add context_window_limit and max_tokens to UpdateAgent [LET-3743] [LET-3741] ([a841c73](https://github.com/letta-ai/letta-python/commit/a841c7333841aa79a70b805b9373b88429db1922))

## 1.0.0-alpha.6 (2025-10-22)

Full Changelog: [v0.0.1...v1.0.0-alpha.6](https://github.com/letta-ai/letta-python/compare/v0.0.1...v1.0.0-alpha.6)

### Features

* add new tool fields to helpers ([#23](https://github.com/letta-ai/letta-python/issues/23)) ([e51d3a7](https://github.com/letta-ai/letta-python/commit/e51d3a7078e82e30b8e0da89c4e60260f61a6fc4))
* add pip requirements to create/upsert_from_func ([#20](https://github.com/letta-ai/letta-python/issues/20)) ([190c493](https://github.com/letta-ai/letta-python/commit/190c493b8a7844ead8cfdec1c986c48723c65d05))


### Bug Fixes

* make tools client async ([#16](https://github.com/letta-ai/letta-python/issues/16)) ([c88e8dd](https://github.com/letta-ai/letta-python/commit/c88e8ddc175d6c1d7d872908907d701b936173aa))


### Chores

* sync repo ([e59730b](https://github.com/letta-ai/letta-python/commit/e59730bb7e0cff18c984f692250e4d0d5f1985eb))
* update poetry download step in workflow ([#22](https://github.com/letta-ai/letta-python/issues/22)) ([dfa262a](https://github.com/letta-ai/letta-python/commit/dfa262aa4fec42ade045e9a41ffb62b37986bab9))
* update SDK settings ([4763bfe](https://github.com/letta-ai/letta-python/commit/4763bfe2245828c3ec8b09427a7d0893ab10dc85))
* update SDK settings ([b54a23a](https://github.com/letta-ai/letta-python/commit/b54a23a21356915fa530c6e29494aa2964741762))
