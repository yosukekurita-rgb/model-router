# Model Router

Model Router is an Agent Skills execution-policy skill, not a model benchmark or cheapest-model selector. It decides how a task should be executed before resolving which concrete runtime, provider, model, and tools should run it.

Do not start by asking which model should do the task. First decide how the task should be executed.

## Why this exists

Many model routers focus primarily on selecting a model:

```text
task
→ pick a model
```

This project deliberately treats model selection as one step in a broader execution decision:

```text
task
→ success criteria and quality target
→ deterministic or probabilistic execution
→ capability requirements
→ depth or breadth
→ single-agent or bounded parallel topology
→ runtime, provider, model, and tools
→ verification
→ residual uncertainty
→ escalation when justified
```

The result is an Agent Skills-compatible bundle that keeps stable policy separate from volatile model and runtime information. Concrete resolution happens only after discovery in the current host; example registries are documentation, not runtime truth.

## What it routes

- deterministic processing versus LLM reasoning;
- required capabilities and eligibility constraints;
- compute and reasoning depth;
- single-agent versus bounded multi-agent topology;
- runtime, provider, model, and tools;
- verification strategy;
- fallback and degraded execution;
- checkpointing and observability when justified;
- human escalation.

## What it does not do

This project is not:

- a universal model benchmark;
- a static model ranking;
- a cheapest-model selector;
- an automatic permission or approval system;
- a replacement for deterministic tests;
- a reason to use multi-agent execution by default;
- a guarantee that every host exposes the requested controls.

## Core routing flow

1. Define required output, success criteria, quality, and verification.
2. Reduce deterministic work before using model reasoning.
3. Express the remaining need as provider-neutral capabilities.
4. Distinguish depth from breadth.
5. Start with one capable agent.
6. Use bounded parallelism only for independent breadth.
7. Discover current eligible runtimes, models, and tools.
8. Execute and verify with observable evidence.
9. Address material residual uncertainty with targeted additional compute, review, or escalation.
10. Stop when the target is met or a policy boundary requires escalation.

See [SKILL.md](SKILL.md) for the executable instructions and [the glossary](references/GLOSSARY.md) for terminology.

## Examples

- [Deterministic data processing](examples/deterministic-data-processing.md): reduce and verify 100,000 CSV rows without using an LLM for core processing.
- [Architecture decision](examples/architecture-decision.md): treat a coupled, high-switching-cost decision as depth and start single-agent.
- [Multi-repository review](examples/multi-repository-review.md): use bounded parallelism for five independent repositories.
- [High-risk change](examples/high-risk-change.md): route a partly reversible permission change through verification, rollback, and authority checks.

## Installation and usage

The setup is short enough to keep in this README. A separate installation guide can be added later if the package gains host-specific installers or configuration steps.

### Install

Install the complete repository as a skill directory named `model-router`. Do not copy only `SKILL.md`: the relative references, examples, evals, and validator are part of the package.

For a Codex repository-local installation:

```bash
mkdir -p .agents/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .agents/skills/model-router
```

For a Codex user-wide installation:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.agents/skills/model-router"
```

Other compatible hosts may use different discovery locations. Keep the complete repository together and follow that host's current skill documentation.

### What must be edited

No file edit is required for a normal installation. In particular, do not rewrite the stable policy in `SKILL.md` to hard-code a provider, model name, price, or capability claim.

The files ending in `.example.yaml` are optional templates, not live configuration automatically consumed by the skill. Customize them only if you intentionally maintain a separate, current environment registry. Verify volatile values against authoritative sources, and do not commit credentials, secrets, or machine-specific private paths.

Edit `agents/openai.yaml` only when you deliberately want to change the displayed name, short description, or default prompt for an OpenAI host. These UI changes do not change the routing policy in `SKILL.md`.

If you ask an AI agent to install the skill, use a bounded instruction such as:

```text
Install the complete repository https://github.com/yosukekurita-rgb/model-router
as .agents/skills/model-router. Do not copy only SKILL.md and do not replace
example registry values with unverified data. Run the repository validator and
report the observed result separately from runtime discovery and invocation.
```

### Verify the installation

From the installed skill directory, install the validation dependency once and run the static validator:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

A passing validator confirms the package structure and static contracts. Confirm runtime discovery separately: in Codex CLI or IDE, run `/skills` or type `$` and check that `model-router` appears. If an update is not detected, restart Codex. Finally, invoke the skill once; installation, discovery, and actual invocation are separate verification states.

### Invoke the skill

For explicit invocation in Codex CLI or IDE, mention the skill with `$model-router`:

```text
$model-router choose an execution strategy for reviewing five independent repositories.
```

In ChatGPT, type `@`, select **Model Router**, and then enter the task. Compatible hosts may also invoke the skill implicitly when the request matches the description in `SKILL.md`.

Use this skill when the execution arrangement itself must be chosen or compared—for example, depth versus breadth, deterministic processing versus model work, fallback after a preferred runtime becomes unavailable, or added verification for a high-risk change. Ordinary work with an already-clear runtime and topology should not trigger it.

See [OpenAI's current skills documentation](https://learn.chatgpt.com/docs/build-skills) or your host's documentation for current discovery locations and invocation syntax.

## インストールと使い方

現時点の導入手順は短いため、このREADMEにまとめています。ホスト別のインストーラーや設定手順が増えた場合は、独立した導入ガイドへ分離します。

### インストール

リポジトリ全体を、`model-router`という名前のスキルディレクトリとして配置してください。`SKILL.md`だけをコピーしてはいけません。相対参照先、使用例、評価ケース、検証スクリプトもパッケージの一部です。

Codexで特定のリポジトリだけに導入する場合:

```bash
mkdir -p .agents/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .agents/skills/model-router
```

Codexでユーザー共通のスキルとして導入する場合:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.agents/skills/model-router"
```

ほかの対応ホストでは、スキルの検出場所が異なる場合があります。リポジトリ全体を同じディレクトリに保ったうえで、各ホストの最新ドキュメントに従ってください。

### 導入時に編集するもの

通常の導入では、ファイルの編集は必要ありません。特に、`SKILL.md`の安定ポリシーへ特定のプロバイダー、モデル名、料金、能力評価を直接書き込まないでください。

`.example.yaml`で終わるファイルは任意のテンプレートであり、このスキルが自動で読み込む実際の設定ファイルではありません。最新の環境レジストリを別途管理する場合にだけ利用してください。変動する値は一次情報で確認し、認証情報、秘密情報、端末固有の非公開パスはコミットしないでください。

`agents/openai.yaml`を編集するのは、OpenAIホスト上の表示名、短い説明、既定プロンプトを意図的に変える場合だけです。UI用メタデータを変えても、`SKILL.md`のルーティングポリシーは変わりません。

AIエージェントに導入を依頼する場合は、たとえば次のように範囲を限定して指示します。

```text
https://github.com/yosukekurita-rgb/model-router のリポジトリ全体を
.agents/skills/model-router に導入してください。SKILL.mdだけをコピーせず、
未検証の値でサンプルレジストリを書き換えないでください。リポジトリ検証を実行し、
その結果と、実行環境での検出・呼び出し確認を分けて報告してください。
```

### 導入を確認する

導入したスキルのディレクトリで、検証用の依存関係を一度導入し、静的検証を実行します。

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

検証成功で確認できるのは、パッケージ構造と静的契約です。実行環境での検出は別に確認してください。Codex CLIまたはIDEでは、`/skills`を実行するか`$`を入力し、`model-router`が表示されることを確認します。更新が反映されない場合はCodexを再起動してください。最後に一度呼び出し、導入済み・検出済み・実際に呼び出された状態を区別します。

### スキルを呼び出す

Codex CLIまたはIDEで明示的に呼び出す場合は、`$model-router`を指定します。

```text
$model-router 5つの独立したリポジトリをレビューする実行戦略を決めて。
```

ChatGPTでは`@`を入力して **Model Router** を選び、その後に依頼を書きます。対応ホストは、依頼が`SKILL.md`のdescriptionに合致すると判断した場合、スキルを暗黙に呼び出すこともあります。

このスキルは、実行方法そのものを選択・比較する必要がある場合に使います。たとえば、深掘りと並列化の選択、決定論的処理とモデル処理の切り分け、優先ランタイムが使えない場合の代替、または高リスク変更に対する検証強化です。実行環境と構成がすでに明確な通常作業では、呼び出す必要はありません。

現在の検出場所や呼び出し構文は、[OpenAIのスキルドキュメント（英語）](https://learn.chatgpt.com/docs/build-skills)または各ホストのドキュメントを確認してください。

## Repository structure

```text
model-router/
├── .github/
│   └── workflows/
│       └── validate.yml
├── README.md
├── SKILL.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── assets/
│   └── ai-environment.example.yaml
├── references/
│   ├── GLOSSARY.md
│   ├── SOURCES.md
│   ├── policies/
│   ├── registry/
│   ├── adapters/
│   ├── workflows/
│   ├── profiles/
│   └── run-recording.md
├── examples/
├── evals/
│   ├── routing-cases.yaml
│   └── trigger-cases.md
├── scripts/
│   └── validate_repository.py
└── requirements-dev.txt
```

## Evaluation

[`evals/routing-cases.yaml`](evals/routing-cases.yaml) contains 20 routing cases covering deterministic reduction, depth, breadth, fallback, data eligibility, verification, and escalation. [`evals/trigger-cases.md`](evals/trigger-cases.md) covers expected invocation, expected non-invocation, and prohibited routing behavior.

Install the single validation dependency once, then run the local static contract validation:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

The script validates package metadata, YAML parsing, relative Markdown links, repository references, the 20 route outcomes against the canonical contract in `SKILL.md`, example route blocks, and encoded negative-behavior guards. CI runs the same command on pull requests and pushes to `main`.

These checks are static contract validation. The eval files remain behavioral specifications: a passing command does not prove that a host discovered, invoked, or followed the skill at runtime.

## Design principles

- quality target first;
- deterministic reduction first;
- capability-based, provider-neutral requirements;
- depth and breadth are different problems;
- single-agent first;
- bounded parallelism for independent work only;
- deterministic verification before semantic review when available;
- explicit residual uncertainty and escalation;
- stable policy separated from volatile registries and adapters;
- stop when additional compute no longer improves the decision.

## Limitations

- This v0.1 package does not include an executable live router or model selector; the host interprets the skill instructions.
- Concrete model, pricing, context, effort, and availability data change and must be discovered or refreshed at runtime.
- Example registries are documentation, not recommendations or runtime truth.
- Host support for model overrides, reasoning controls, subagents, tool restrictions, tracing, and cross-model review varies.
- Logical routing cannot grant permission or approval.
- Semantic work may retain uncertainty even after the best available verification.

## License

This project is licensed under the [MIT License](LICENSE).
