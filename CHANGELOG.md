# Changelog

## 1.3.1 (2025-11-26)

Full Changelog: [v1.3.0...v1.3.1](https://github.com/letta-ai/letta-python/compare/v1.3.0...v1.3.1)

### Features

* Fix template alignment ([0380268](https://github.com/letta-ai/letta-python/commit/0380268aab9df514c7d0948e9c31b63953d7b249))
* query param validation block label, name, and search ([9559f56](https://github.com/letta-ai/letta-python/commit/9559f56e0374603ff3977ee6952b3fb691ab9163))
* run tool by  for a given agent ([4706b60](https://github.com/letta-ai/letta-python/commit/4706b6010115f3a89c82674d40ce7277663c332b))
* Shub/let 6339 add endpoint for counting non hidden agents [LET-6339] ([cfee192](https://github.com/letta-ai/letta-python/commit/cfee1925329419dfd1f2f65b6e47b74bc24781de))
* structured outputs for anthropic ([7dd7254](https://github.com/letta-ai/letta-python/commit/7dd72547133d23e171c6bf9d27d54631a10eb144))
* structured outputs for openai [LET-6233] ([96e56fa](https://github.com/letta-ai/letta-python/commit/96e56fa56612e293d8b7beef6e3d74a216ea07f2))


### Chores

* add tools search to stainless ([e1dfa06](https://github.com/letta-ai/letta-python/commit/e1dfa064626578158483db163d511af7f153d921))

## 1.3.0 (2025-11-25)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/letta-ai/letta-python/compare/v1.2.0...v1.3.0)

### Features

* add messages + passages to stainless.yml ([44aac08](https://github.com/letta-ai/letta-python/commit/44aac08d1d31a4fa1cb7f805dd5de9744c674daa))


### Chores

* use main branch in sdk repos ([b71fff8](https://github.com/letta-ai/letta-python/commit/b71fff88a4c194f478fe3e5fc0ac1430607c1947))

## 1.2.0 (2025-11-25)

Full Changelog: [v1.1.2...v1.2.0](https://github.com/letta-ai/letta-python/compare/v1.1.2...v1.2.0)

### Features

* add search routes ([71094b3](https://github.com/letta-ai/letta-python/commit/71094b371fc636bdc3a8956ce36793b8218a96e0))
* add support for new model ([03a1d2d](https://github.com/letta-ai/letta-python/commit/03a1d2d9c7fc4b3ba4b7aa14020c3ef5118d5506))


### Bug Fixes

* disable messages + passages for now ([f6c4e54](https://github.com/letta-ai/letta-python/commit/f6c4e545e0eac72f03829cfd08da2e8dfa37b2b0))
* properly limit runs query ([eccc942](https://github.com/letta-ai/letta-python/commit/eccc942c424192fed7993024b88edb37b130e434))


### Chores

* add Python 3.14 classifier and testing ([4d3c6e8](https://github.com/letta-ai/letta-python/commit/4d3c6e851c009dcb1aa667e459df4788cadf050b))

## 1.1.2 (2025-11-21)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/letta-ai/letta-python/compare/v1.1.1...v1.1.2)

### Bug Fixes

* api key not optional for stainless sdk ([6ef0456](https://github.com/letta-ai/letta-python/commit/6ef04566b0e8a0924132684ab22d0a96620f2e28))

## 1.1.1 (2025-11-21)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/letta-ai/letta-python/compare/v1.1.0...v1.1.1)

### Features

* parallel tool calling in model settings ([d9fb097](https://github.com/letta-ai/letta-python/commit/d9fb0970aff1e28599f0ed14a69db2127919ce00))


### Bug Fixes

* create agent for template openapi response schema ([adb1515](https://github.com/letta-ai/letta-python/commit/adb151525142f77e4fcd1331cf8e5e0a17e20f87))

## 1.1.0 (2025-11-20)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/letta-ai/letta-python/compare/v1.0.0...v1.1.0)

### Features

* add new letta error message stream response type ([dfa5f65](https://github.com/letta-ai/letta-python/commit/dfa5f6577d26e9b0ad684ebb9123cbbd1637f06d))
* rename upsert properties endpoint ([7764513](https://github.com/letta-ai/letta-python/commit/7764513a9cf431e4ee97e2e63e11804de480f06f))

## 1.0.0 (2025-11-19)

Full Changelog: [v1.0.0-alpha.22...v1.0.0](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.22...v1.0.0)

### Features

* add client side access tokens to stainless ([770bfdb](https://github.com/letta-ai/letta-python/commit/770bfdbbd9e77ce0d305295f8c081ca03e6971c0))
* hack at gpt51 [LET-6178] ([d93a58c](https://github.com/letta-ai/letta-python/commit/d93a58c390c7995cecd890667c76d393dd8834b8))
* Revert "feat: support anthropic structured outputs [LET-6190]" ([e3aed33](https://github.com/letta-ai/letta-python/commit/e3aed33178bf71fa15e5e739a908cb5bc85d03f4))

## 1.0.0-alpha.22 (2025-11-18)

Full Changelog: [v1.0.0-alpha.21...v1.0.0-alpha.22](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.21...v1.0.0-alpha.22)

### Features

* make config for mcp_servers and messages.modify nested ([8d9ec52](https://github.com/letta-ai/letta-python/commit/8d9ec52526ede5a82bc950bce56937dba1c2ac1a))


### Bug Fixes

* make attach/detach routes return None if sdk verion 1.0 ([c8496f1](https://github.com/letta-ai/letta-python/commit/c8496f1fb953b75bc08ea4bbcf61884d5a50c747))

## 1.0.0-alpha.21 (2025-11-17)

Full Changelog: [v1.0.0-alpha.20...v1.0.0-alpha.21](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.20...v1.0.0-alpha.21)

### Features

* make attach/detach routes return None if version is 1.0 [LET-5844] ([799aa31](https://github.com/letta-ai/letta-python/commit/799aa31b7124a3d9841d3153aff09457d47bded6))
* move sources to folders ([4b86f41](https://github.com/letta-ai/letta-python/commit/4b86f41014ad19c7751039ad718f7ed3542c8d1a))
* rename .af parameters [LET-6154] ([90c47e6](https://github.com/letta-ai/letta-python/commit/90c47e6d4bb58e9054c8c63f1707bff086165d06))
* Revert "feat: make attach/detach routes return None if version is 1.0 [LET-5844]" ([417acb3](https://github.com/letta-ai/letta-python/commit/417acb3c34d6da398a9feb0a2c247f6062703277))
* support anthropic structured outputs [LET-6190] ([626a22c](https://github.com/letta-ai/letta-python/commit/626a22c4ebc3030072155b84e4c8cb4062a9dae3))


### Chores

* remove mcp-servers connect for stainless [LET-6166] ([9f1072b](https://github.com/letta-ai/letta-python/commit/9f1072b5998452ac8fd376bf36729c50981e98ba))
* rename summarize to compact in sdk ([48a3217](https://github.com/letta-ai/letta-python/commit/48a32175cf56f655b02cc25fc62b2861ed2def8d))

## 1.0.0-alpha.20 (2025-11-12)

Full Changelog: [v1.0.0-alpha.19...v1.0.0-alpha.20](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.19...v1.0.0-alpha.20)

### Features

* deprecate `EmbeddingConfig` from archives ([d6cbbc3](https://github.com/letta-ai/letta-python/commit/d6cbbc39933572367b06194c87affcf35d2c38f6))


### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([4724b32](https://github.com/letta-ai/letta-python/commit/4724b328a03756d769f38f5939604131a67ac83d))


### Chores

* rename send to create and modify to update ([c8e0661](https://github.com/letta-ai/letta-python/commit/c8e0661e694c3511239e806bffba3ef7cda69d25))
* update stainless send to create ([7f55f59](https://github.com/letta-ai/letta-python/commit/7f55f59807e6a2483ce7ae38bff92f16eb40b5b4))

## 1.0.0-alpha.19 (2025-11-12)

Full Changelog: [v1.0.0-alpha.18...v1.0.0-alpha.19](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.18...v1.0.0-alpha.19)

### Features

* add approval return param to stainless ([5753672](https://github.com/letta-ai/letta-python/commit/5753672ae96a9885bbcc5838f76de3364c28a743))
* add attach detach methods for archives and identities to sdk ([a8d22bc](https://github.com/letta-ai/letta-python/commit/a8d22bc5b5925c10c769d126f4498a7656690115))
* add create memory for archive ([07cefb6](https://github.com/letta-ai/letta-python/commit/07cefb6cb6a446d7df976d5111490957e1b52f73))
* add model setting params to stainless config ([ee056aa](https://github.com/letta-ai/letta-python/commit/ee056aaf33270f163cb0dd44f8834c7f61e6f9a5))
* add passage deletion route to sdk ([b932046](https://github.com/letta-ai/letta-python/commit/b932046e52020ccdc831a6a79d6b428854039fc3))
* bring back model_settings and remove validation again ([9189431](https://github.com/letta-ai/letta-python/commit/9189431a6611060358f14d559dc6b951fa6487bd))
* make api key optional in sdk ([0e12938](https://github.com/letta-ai/letta-python/commit/0e129388fc55a00f1ec4dbd341f673337b4fef8d))
* rename message union and internal message ([c4d750b](https://github.com/letta-ai/letta-python/commit/c4d750bf05d140ed432f6234b3888a6b74fce346))
* revert model_settings ([5402070](https://github.com/letta-ai/letta-python/commit/5402070ee145fc75464419de54bdef6067d822f6))


### Bug Fixes

* compat with Python 3.14 ([9ea3e28](https://github.com/letta-ai/letta-python/commit/9ea3e28969236c7cea352e01f5b12b3112217b12))


### Chores

* api sync ([ce3a822](https://github.com/letta-ai/letta-python/commit/ce3a82265ef1ed1c3b322c045801aa185b4b8d6a))
* **package:** drop Python 3.8 support ([6d5b749](https://github.com/letta-ai/letta-python/commit/6d5b749e8e162be7d642ecd438843474c77f1908))
* reorder stainless SDK ([9b09499](https://github.com/letta-ai/letta-python/commit/9b09499a5106c58739f3c60ef7b63956ba8f0fe2))

## 1.0.0-alpha.18 (2025-11-10)

Full Changelog: [v1.0.0-alpha.17...v1.0.0-alpha.18](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.17...v1.0.0-alpha.18)

### Features

* add list support for query params in sdk ([72ce7fa](https://github.com/letta-ai/letta-python/commit/72ce7fabf7194a489df67c65a2cbe00eedb69c15))


### Bug Fixes

* prevent too many runs bug ([d9ed0ca](https://github.com/letta-ai/letta-python/commit/d9ed0caf11dfe24daaf4c57a307ebd4330049284))

## 1.0.0-alpha.17 (2025-11-08)

Full Changelog: [v1.0.0-alpha.16...v1.0.0-alpha.17](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.16...v1.0.0-alpha.17)

### Features

* add model settings schema to stainless [LET-5976] ([69bfb1c](https://github.com/letta-ai/letta-python/commit/69bfb1c79aa585199c916ee3fce16fa061455f6a))
* chore; regen ([72d9f8f](https://github.com/letta-ai/letta-python/commit/72d9f8fe99bced01c266c3d7273db2b5918fa912))
* split up handle and `model_settings` ([c5ada9d](https://github.com/letta-ai/letta-python/commit/c5ada9de94ff2c33171c6db4e0676548f1b6186f))


### Chores

* add model and embedding models ([5f488eb](https://github.com/letta-ai/letta-python/commit/5f488eb7206121076b08dd78725d8834f1aab5ad))

## 1.0.0-alpha.16 (2025-11-07)

Full Changelog: [v1.0.0-alpha.15...v1.0.0-alpha.16](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.15...v1.0.0-alpha.16)

### Features

* add filters to count_agents endpoint [LET-5380] [LET-5497] ([1c2e09f](https://github.com/letta-ai/letta-python/commit/1c2e09f64d6858de3caf9cce921ce12527fdf988))
* add last_stop_reason to AgentState [LET-5911] ([68b054a](https://github.com/letta-ai/letta-python/commit/68b054a8aa29491948d22e2ffd5498396833b0d1))
* enable streaming flag on send message ([4984f2d](https://github.com/letta-ai/letta-python/commit/4984f2d183b5353ca6f47ca7d5cdd83b971dcc13))
* filter list agents by stop reason [LET-5928] ([d2316ce](https://github.com/letta-ai/letta-python/commit/d2316cecbca3d31f3a46217f8eb3b8d47fb6664d))
* return new Model and EmbeddingModel objects for list model/embedding endpoints [LET-6090] ([bd729a3](https://github.com/letta-ai/letta-python/commit/bd729a341841559887ace72b516d1d4ef82a5ab4))
* Revert "Revert "feat: provider-specific model configuration " ([#5873](https://github.com/letta-ai/letta-python/issues/5873))" ([83f4534](https://github.com/letta-ai/letta-python/commit/83f4534bc86a7e6018ff874fd137592ad0a94549))


### Bug Fixes

* add mcp server routes typing to stainless.yml ([a4f5fd0](https://github.com/letta-ai/letta-python/commit/a4f5fd016322f1c84790a7d1e080456b42763350))
* **core:** patch bug w/ sleeptime agents and client-side tool executions [LET-6081] ([ee84c56](https://github.com/letta-ai/letta-python/commit/ee84c565d23c5b8eea385bc89a3af74a987982e8))
* fix refresh sdk name stainless ([83f446d](https://github.com/letta-ai/letta-python/commit/83f446debf5dba3150e5f8c56db73d3490677259))
* stainless pagination ([a99ce51](https://github.com/letta-ai/letta-python/commit/a99ce5137600be328f040e42ef3a1c8e32827e63))


### Chores

* remove count methods from stainless sdk ([3bfe0c7](https://github.com/letta-ai/letta-python/commit/3bfe0c72c26dfc7f648e75b585566604e25315cd))

## 1.0.0-alpha.15 (2025-11-04)

Full Changelog: [v1.0.0-alpha.14...v1.0.0-alpha.15](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.14...v1.0.0-alpha.15)

### Features

* add `EventMessage` and `SummaryMessage` ([543571c](https://github.com/letta-ai/letta-python/commit/543571ccdfd7f416c7ed4aca44007155019ed424))
* add input option to send message route [LET-4540] ([566914d](https://github.com/letta-ai/letta-python/commit/566914db30baedd9354813fccc48dd17483a98e8))
* make sure tool return chars within max int range ([4c90f6d](https://github.com/letta-ai/letta-python/commit/4c90f6dacfe214aede582881c264fbad5f5bc99c))

## 1.0.0-alpha.14 (2025-11-04)

Full Changelog: [v1.0.0-alpha.13...v1.0.0-alpha.14](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.13...v1.0.0-alpha.14)

### Features

* add new project id header to stainless client ([144fd56](https://github.com/letta-ai/letta-python/commit/144fd562594a87620b4e17ad85cade425ae2391d))


### Bug Fixes

* enable stainless pagination ([f4f5744](https://github.com/letta-ai/letta-python/commit/f4f574416331aeb6b48e929b5d589417d14a3c7b))


### Chores

* **internal:** grammar fix (it's -&gt; its) ([d8f60b1](https://github.com/letta-ai/letta-python/commit/d8f60b16cd7fc47cbaddcb8de057a25ff7731fae))
* update stainless templates route to not pass in project id ([a0ba998](https://github.com/letta-ai/letta-python/commit/a0ba9981d73b13a7e5c2995691679696daeae9b6))

## 1.0.0-alpha.13 (2025-11-03)

Full Changelog: [v1.0.0-alpha.12...v1.0.0-alpha.13](https://github.com/letta-ai/letta-python/compare/v1.0.0-alpha.12...v1.0.0-alpha.13)

### Features

* add stream return type to all sse endpoints ([7fd0583](https://github.com/letta-ai/letta-python/commit/7fd05834ac10672a2dbb6912c2b453167a27eff1))

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
