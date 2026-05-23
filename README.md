IMRCのロボット全体状態管理ノードです。

現在の自動制御フェーズ、
保持しているボール数などの状態情報を管理し、
ROS2 Topicを通じて各ノードへ配信します。

また、imrc_conpanelからの操作入力を受け取り、
状態更新も行います。

---

## 機能

- 自動制御フェーズ管理
- ボール保持数管理
- 状態情報配信
- 操作入力による状態更新
- ROS2 Topic通信

---

## 管理情報例

- 現在のフェーズ番号
- ボール保持数
- 動作状態
- 手動/自動モード

---

## システム構成

```text
[imrc_conpanel]
        │
        ▼
[imrc_progress_manager]
        │
        ├── Status Publish
        ├── Phase Publish
        └── Ball Count Publish
