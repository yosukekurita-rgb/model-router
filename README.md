# Model Router

[English](#english) | [日本語](#日本語) | [Technical reference](#technical-reference)

## English

Model Router is an Agent Skills execution-policy skill. Install it when you want an AI agent to decide how a task should be executed before choosing a concrete runtime, provider, model, or tool.

It is not a live model-switching service. It gives the host agent a reusable decision policy and a verifiable execution plan.

### What you can do after installation

Ask Model Router to decide:

- which parts should use deterministic tools such as parsers, queries, scripts, static analysis, or tests before an LLM is involved;
- whether the task needs deeper reasoning, more context, independent breadth, or an external dependency;
- whether one capable agent is enough or bounded parallel work is justified;
- which provider-neutral capabilities a runtime, model, and tool set must provide;
- how much compute or reasoning effort the quality target warrants;
- how the result should be verified, observed, and recorded;
- what fallback remains valid if the preferred runtime or tool is unavailable; and
- whether uncertainty, risk, or authority requires a human decision.

### Problems it solves

Model Router addresses recurring execution-design failures:

- choosing a model before defining success and verification;
- sending deterministic core processing to an LLM;
- adding agents to one coupled bottleneck that cannot be parallelized safely;
- treating a stale model list or benchmark as current runtime truth;
- silently lowering quality when the preferred route fails;
- treating an AI's success statement as verification; and
- confusing technical availability with permission or policy eligibility.

### What makes it different

- **Stable policy contains no concrete model names.** Model availability, pricing, context limits, and controls are discovered at execution time, so the policy does not become stale whenever a provider changes its catalog.
- **Capability escalation and authority escalation are separate decisions.** A task may need a stronger model, more context, or a specialist without needing more permission; conversely, an irreversible action may require approval even when its technical execution is easy.
- **Operational control is part of routing.** “Approval requested” is not “approval granted,” availability is not permission, and data eligibility is checked before a runtime or tool becomes a valid candidate.

### What you receive

The skill returns an execution route that states the quality target, required capabilities, deterministic-first work, limiting shape, agent topology, compute profile, runtime resolution, verification method, observability, escalation, assumptions, and residual uncertainty.

For example, instead of only answering “use model X,” it can recommend:

```text
deterministic preprocessing
→ one capable agent with deep reasoning
→ mixed test and semantic verification
→ human approval before an irreversible action
```

The canonical machine-readable outcome is defined in [SKILL.md](SKILL.md).

### Typical requests

```text
$model-router Decide whether this 100,000-row CSV task needs an LLM at all.
$model-router Should five independent repositories be reviewed by one agent or bounded parallel agents?
$model-router The preferred runtime is unavailable. Find a fallback without lowering the quality target.
$model-router Design a verifiable execution route for a high-risk permission change.
```

### Supported hosts

Model Router is not Codex-only. Its policy, references, examples, and route schema are provider-neutral Agent Skills content.

- **Codex** discovers the skill from `.agents/skills/` and maps the logical route through the [Codex adapter](references/adapters/codex.md).
- **Claude Code** follows the Agent Skills standard, discovers the skill from `.claude/skills/`, and maps the route through the [Claude Code adapter](references/adapters/claude-code.md).
- **ChatGPT** can invoke an installed skill explicitly with `@` or implicitly from its description. Personal skill availability and upload permissions depend on the ChatGPT plan and workspace settings.
- Other Agent Skills-compatible hosts may work when they support a multi-file skill directory and its relative references. Verify their discovery and invocation rules separately.

The `agents/openai.yaml` file contains optional OpenAI UI metadata. It does not make the routing policy Codex-specific. Concrete controls still vary by host, so static package validation does not prove runtime discovery or invocation.

Do not start by asking which model should do the task. First decide how the task should be executed.

### How it works

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

### What it does not do

This project is not:

- a universal model benchmark;
- a static model ranking;
- a cheapest-model selector;
- an automatic permission or approval system;
- a replacement for deterministic tests;
- a reason to use multi-agent execution by default;
- a guarantee that every host exposes the requested controls.

### Core routing flow

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

### Examples

- [Deterministic data processing](examples/deterministic-data-processing.md): reduce and verify 100,000 CSV rows without using an LLM for core processing.
- [Architecture decision](examples/architecture-decision.md): treat a coupled, high-switching-cost decision as depth and start single-agent.
- [Multi-repository review](examples/multi-repository-review.md): use bounded parallelism for five independent repositories.
- [High-risk change](examples/high-risk-change.md): route a partly reversible permission change through verification, rollback, and authority checks.

### Installation and usage

Install the complete repository as a skill directory named `model-router`. Do not copy only `SKILL.md`: its references, examples, evals, adapters, and validator are part of the package.

Run project-local commands from the root of the project where you want to use the skill.

#### Codex

Project-local installation:

```bash
mkdir -p .agents/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .agents/skills/model-router
```

User-wide installation:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.agents/skills/model-router"
```

OpenAI documents these as the current local-skill locations. We also opened `/skills` in Codex CLI 0.151.0 and confirmed both a project-local Model Router under `$CWD/.agents/skills` and a user skill under `$HOME/.agents/skills`. Because `$HOME/.codex/skills` is not listed as a current local-skill location, this guide does not use it.

See [OpenAI's Codex skills documentation](https://developers.openai.com/codex/skills) for current discovery behavior.

#### Claude Code

Project-local installation:

```bash
mkdir -p .claude/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .claude/skills/model-router
```

User-wide installation:

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.claude/skills/model-router"
```

Claude Code can select the skill automatically from its description or invoke it directly as `/model-router`. If `.claude/skills/` did not exist when the current session started, restart Claude Code after creating it. See [Anthropic's Claude Code skills documentation](https://code.claude.com/docs/en/skills) for current behavior.

#### ChatGPT

ChatGPT personal skills are currently available only to eligible Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability. If your workspace permits skill uploads:

1. Download a ZIP archive of the complete repository. Do not upload only `SKILL.md`.
2. In ChatGPT, open **Plugins** in the sidebar and select the **Skills** tab.
3. Select **Create**, then **Upload from your computer**, and choose the archive.
4. Wait for ChatGPT's scan to finish. Review any **Needs Review** result before using the skill; a **Blocked** result cannot be installed.
5. Confirm that **Model Router** appears in the installed skills list.

See [OpenAI's ChatGPT skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for current eligibility, upload, and workspace-control details. Installation and syncing can differ between ChatGPT and Codex, so verify each product separately.

Other compatible hosts may use different discovery locations. Keep the complete repository together and follow that host's documentation.

#### What must be edited

No file edit is required for a normal installation. In particular, do not rewrite the stable policy in `SKILL.md` to hard-code a provider, model name, price, or capability claim.

The files ending in `.example.yaml` are optional templates, not live configuration automatically consumed by the skill. Customize them only if you intentionally maintain a separate, current environment registry. Verify volatile values against authoritative sources, and do not commit credentials, secrets, or machine-specific private paths.

Edit `agents/openai.yaml` only when you deliberately want to change the displayed name, short description, or default prompt for an OpenAI host. These UI changes do not change the routing policy in `SKILL.md`.

If you ask an AI agent to install the skill, name the target host and use a bounded instruction such as:

```text
Install the complete repository https://github.com/yosukekurita-rgb/model-router
as a project-local Agent Skill for TARGET_HOST. Use .agents/skills/model-router
for Codex or .claude/skills/model-router for Claude Code. Do not copy only
SKILL.md or replace example registry values with unverified data. Run the
repository validator and report package validation, runtime discovery, and
actual invocation as separate results.
```

#### Verify the installation

From the installed skill directory, install the validation dependency once and run the static validator:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

A passing validator confirms the package structure and static contracts. Confirm runtime discovery and invocation separately:

- In Codex CLI or IDE, run `/skills` or type `$`, confirm that `model-router` appears, and invoke it as `$model-router`.
- In Claude Code, run `/skills`, confirm that `model-router` appears, and invoke it as `/model-router`.
- In ChatGPT, open **Plugins** > **Skills**, confirm that **Model Router** is installed, then type `@` in a chat and select it.

Finally, try one realistic routing request. Installation, static validation, discovery, and actual invocation are separate verification states.

#### Invoke the skill

Codex CLI or IDE:

```text
$model-router choose an execution strategy for reviewing five independent repositories.
```

Claude Code:

```text
/model-router choose an execution strategy for reviewing five independent repositories.
```

In ChatGPT, type `@`, select **Model Router**, and then enter the task. Codex, ChatGPT, and Claude Code may also invoke the skill automatically when the request matches the description in `SKILL.md`.

Use this skill when the execution arrangement itself must be chosen or compared—for example, depth versus breadth, deterministic processing versus model work, fallback after a preferred runtime becomes unavailable, or added verification for a high-risk change. Ordinary work with an already-clear runtime and topology should not trigger it.

See the relevant host documentation for current discovery locations and invocation syntax.

## 日本語

Model Routerは、具体的なモデルを選ぶ前に「この仕事をどう実行するか」を決めるAgent Skills形式のスキルです。導入すると、AIエージェントが仕事に合った実行計画を組み立てられるようになります。計画では、品質目標に合わせて実行手段と検証方法を決めます。代替手段と、人に判断を求める条件も明示します。

モデルを自動で切り替える実行サービスではありません。CodexやClaude Codeなど、スキルを読み込んだホストに再利用可能な判断ポリシーを与えます。

### 導入するとできること

次のような判断をModel Routerへ任せられます。

- LLMを使う前に、パーサー、クエリ、スクリプト、静的解析、テストで処理すべき範囲を切り分ける
- 必要なのが深い推論なのか、広い独立作業なのか、大きなコンテキストなのかを見極める
- 1つの高性能なエージェントで進めるか、範囲を限定して並列化するかを決める
- ランタイム、モデル、ツールに必要な能力を、プロバイダーに依存しない形で定義する
- 品質目標に応じた推論量や計算量を選ぶ
- 結果の検証方法、観測方法、記録レベルを決める
- 優先ランタイムやツールが使えない場合も、品質を勝手に下げずに代替案を作る
- 不確実性、リスク、権限のどれが人の判断を必要としているかを明らかにする

### 解決する問題

- 成功条件や検証方法より先にモデル名を決めてしまう
- 決定論的に処理できる中核作業までLLMへ渡してしまう
- 分割できないボトルネックへエージェントを増やしてしまう
- 古いモデル一覧やベンチマークを現在の利用可否だと誤認する
- 優先ルートの失敗時に、説明なく品質目標を下げてしまう
- AIの「成功しました」という報告を、そのまま検証結果として扱ってしまう
- 技術的に利用できることを、権限やポリシー上も許可されていると誤認する

### 設計上の特徴

- **安定ポリシーに具体的なモデル名を持ち込みません。** モデルの提供状況、料金、コンテキスト上限、操作方法は実行時に発見します。プロバイダーの製品構成が変わっても、判断ポリシーそのものが陳腐化しにくい設計です。
- **能力のエスカレーションと権限のエスカレーションを分けています。** より強いモデルや専門家が必要でも追加承認は不要な場合があります。一方、技術的には簡単でも、不可逆な操作には承認が必要です。
- **IT統制の考え方を実行ルートへ組み込んでいます。** 「承認を依頼した」と「承認された」を区別し、可用性を許可とみなさず、データ適格性を確認してからランタイムやツールを候補にします。

### 得られるもの

得られるのは、どう実行し、どう検証し、どこで止めるかを再現できる実行ルートです。正式な出力には、判断の前提と選択した構成を残します。ランタイムを解決できたか、何が不確実なままか、人の判断がどこで必要かも示します。

たとえば「モデルXを使う」だけで終わらず、次のような計画を返します。

```text
決定論的な前処理
→ 深い推論を行う1つの高性能エージェント
→ テストと意味的レビューを組み合わせた検証
→ 不可逆な操作の直前に人の承認
```

機械可読な正式スキーマは[SKILL.md](SKILL.md)で定義しています。

### 依頼例

```text
10万行のCSV処理で、LLMを使うべき範囲があるか判断して。
独立した5つのリポジトリは、1エージェントと並列エージェントのどちらでレビューすべき？
優先ランタイムが使えない。品質目標を下げない代替ルートを決めて。
権限変更を安全に実行し、検証できるルートを設計して。
```

### 対応ホスト

Model RouterはCodex専用ではありません。中核ポリシーと出力スキーマは、プロバイダーに依存しないAgent Skillsとして作られています。付属の参照資料と使用例も、特定のホストだけを前提にしていません。

- **Codex**は`.agents/skills/`からスキルを検出し、[Codexアダプター](references/adapters/codex.md)で論理ルートを実際の操作へ対応づけます。
- **Claude Code**はAgent Skills標準に対応しており、`.claude/skills/`からスキルを検出します。[Claude Codeアダプター](references/adapters/claude-code.md)でホスト固有の操作へ対応づけます。
- **ChatGPT**では、導入済みのスキルを`@`で明示的に選ぶか、依頼内容に合う場合に暗黙で呼び出せます。パーソナルスキルを利用できるプランとアップロード権限は、契約とワークスペース設定により異なります。
- ほかのAgent Skills対応ホストでも、複数ファイルからなるスキルと相対参照を扱える場合は利用できる可能性があります。検出場所と呼び出し方法はホストごとに確認してください。

`agents/openai.yaml`はOpenAI製品向けの任意のUI情報です。このファイルがあっても、ルーティングポリシーがCodex専用になるわけではありません。なお、静的検証に成功しても、各ホストでの検出や実呼び出しまで証明したことにはなりません。

### 具体例

- [決定論的なデータ処理](examples/deterministic-data-processing.md): 10万行のCSVを、LLMではなく再現可能な処理で集計・検証する
- [アーキテクチャ判断](examples/architecture-decision.md): 分割しにくく手戻りコストの高い判断を、並列化せず1エージェントで深掘りする
- [複数リポジトリのレビュー](examples/multi-repository-review.md): 独立した5つの対象だけを範囲限定で並列化する
- [高リスク変更](examples/high-risk-change.md): 権限、ロールバック、検証、承認を分けて設計する

### インストールと使い方

リポジトリ全体を、`model-router`という名前のスキルディレクトリとして配置してください。`SKILL.md`だけをコピーしてはいけません。参照資料、使用例、評価ケース、アダプター、検証スクリプトもパッケージの一部です。

プロジェクト単位で導入するコマンドは、そのスキルを使いたいプロジェクトのルートで実行してください。

#### Codex

プロジェクト単位で導入する場合:

```bash
mkdir -p .agents/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .agents/skills/model-router
```

ユーザー共通のスキルとして導入する場合:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.agents/skills/model-router"
```

上記はOpenAIが現在案内している保存先です。Codex CLI 0.151.0で`/skills`を開き、`$CWD/.agents/skills`のModel Routerと、`$HOME/.agents/skills`のユーザー用スキルが表示されることも確認しました。`$HOME/.codex/skills`は現在のローカルスキル保存先に含まれていないため、このガイドでは案内しません。

現在の検出仕様は[OpenAIのCodexスキルドキュメント（英語）](https://developers.openai.com/codex/skills)を確認してください。

#### Claude Code

プロジェクト単位で導入する場合:

```bash
mkdir -p .claude/skills
git clone https://github.com/yosukekurita-rgb/model-router.git .claude/skills/model-router
```

ユーザー共通のスキルとして導入する場合:

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/yosukekurita-rgb/model-router.git "$HOME/.claude/skills/model-router"
```

Claude Codeはdescriptionに合う依頼から自動的に選択でき、`/model-router`で明示的に呼び出すこともできます。現在のセッション開始時に`.claude/skills/`が存在していなかった場合は、作成後にClaude Codeを再起動してください。現在の仕様は[AnthropicのClaude Code Skillsドキュメント（英語）](https://code.claude.com/docs/en/skills)を確認してください。

#### ChatGPT

ChatGPTのパーソナルスキルは現在、対象となるBusiness・Enterprise・Healthcare・Eduユーザー向けの機能です。実際に利用できるかは、ワークスペース設定と製品上の提供状況にも左右されます。スキルのアップロードが許可されている場合は、次の手順で導入します。

1. リポジトリ全体をZIP形式でダウンロードします。`SKILL.md`だけをアップロードしないでください。
2. ChatGPTのサイドバーで **Plugins** を開き、**Skills** タブを選びます。
3. **Create**、**Upload from your computer** の順に選び、ZIPファイルをアップロードします。
4. ChatGPTによるスキャンの完了を待ちます。**Needs Review** と表示された場合は内容を確認してください。**Blocked** の場合は導入できません。
5. 導入済みスキルの一覧に **Model Router** が表示されることを確認します。

対象プラン、アップロード、ワークスペース管理の現在の仕様は、[OpenAIのChatGPTスキルガイド（英語）](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)を確認してください。ChatGPTとCodexでは導入状態や同期方法が異なる場合があるため、製品ごとに確認します。

#### 導入時に編集するもの

通常の導入では、ファイルの編集は必要ありません。特に、`SKILL.md`の安定ポリシーへ特定のプロバイダー、モデル名、料金、能力評価を直接書き込まないでください。

`.example.yaml`で終わるファイルは任意のテンプレートであり、このスキルが自動で読み込む実際の設定ファイルではありません。最新の環境レジストリを別途管理する場合にだけ利用してください。変動する値は一次情報で確認し、認証情報、秘密情報、端末固有の非公開パスはコミットしないでください。

`agents/openai.yaml`を編集するのは、OpenAI製品上の表示名、短い説明、既定プロンプトを意図的に変える場合だけです。Claude Codeで使うための編集は不要です。

AIエージェントへ導入を依頼する場合は、対象ホストを明記して次のように指示します。

```text
https://github.com/yosukekurita-rgb/model-router のリポジトリ全体を、
TARGET_HOSTのプロジェクト用Agent Skillとして導入してください。
Codexなら.agents/skills/model-router、Claude Codeなら
.claude/skills/model-routerを使ってください。SKILL.mdだけをコピーせず、
未検証の値でサンプルレジストリを書き換えないでください。
パッケージ検証、実行環境での検出、実呼び出しを分けて報告してください。
```

#### 導入を確認する

導入したスキルのディレクトリで、検証用の依存関係を一度導入し、静的検証を実行します。

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

静的検証に成功したら、検出と実呼び出しを別に確認します。

- Codex CLIまたはIDEでは、`/skills`を実行するか`$`を入力し、`model-router`が表示されることを確認してから`$model-router`で呼び出します。
- Claude Codeでは`/skills`で`model-router`が表示されることを確認してから、`/model-router`で呼び出します。
- ChatGPTでは **Plugins**、**Skills** の順に開いて **Model Router** が導入済みであることを確認し、チャットで`@`から選択します。

最後に、実際の依頼を1件試してください。導入済み、静的検証済み、ホストで検出済み、実際に呼び出された、という状態はそれぞれ別です。

#### スキルを呼び出す

Codex CLIまたはIDE:

```text
$model-router 独立した5つのリポジトリをレビューする実行戦略を決めて。
```

Claude Code:

```text
/model-router 独立した5つのリポジトリをレビューする実行戦略を決めて。
```

ChatGPTでは`@`を入力して **Model Router** を選び、その後に依頼を書きます。Codex、ChatGPT、Claude Codeはいずれも、依頼が`SKILL.md`のdescriptionに合う場合に自動選択できる可能性があります。

実行環境と構成がすでに明確な通常作業では、このスキルを呼び出す必要はありません。

## Technical reference

### Repository structure

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

### Evaluation

[`evals/routing-cases.yaml`](evals/routing-cases.yaml) contains 20 routing cases covering deterministic reduction, depth, breadth, fallback, data eligibility, verification, and escalation. [`evals/trigger-cases.md`](evals/trigger-cases.md) covers expected invocation, expected non-invocation, and prohibited routing behavior.

Install the single validation dependency once, then run the local static contract validation:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

The script validates package metadata, YAML parsing, relative Markdown links, repository references, the 20 route outcomes against the canonical contract in `SKILL.md`, example route blocks, and encoded negative-behavior guards. CI runs the same command on pull requests and pushes to `main`.

These checks are static contract validation. The eval files remain behavioral specifications: a passing command does not prove that a host discovered, invoked, or followed the skill at runtime.

### Design principles

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

### Limitations

- This v0.1 package does not include an executable live router or model selector; the host interprets the skill instructions.
- Concrete model, pricing, context, effort, and availability data change and must be discovered or refreshed at runtime.
- Example registries are documentation, not recommendations or runtime truth.
- Host support for model overrides, reasoning controls, subagents, tool restrictions, tracing, and cross-model review varies.
- Logical routing cannot grant permission or approval.
- Semantic work may retain uncertainty even after the best available verification.

### License

This project is licensed under the [MIT License](LICENSE).
