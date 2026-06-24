# Tractatus Code — リファクタリング例

# === BEFORE: 語りえぬものを語ろうとしている ===

# ユーザーのアクセス権限をチェックする関数
# status が active かつ role が admin で suspended でなければアクセス許可
def check_access(user):
    # status を確認
    if user.get("status") == "active":
        # role を確認
        if user.get("role") == "admin":
            # suspended フラグを確認
            if not user.get("suspended", False):
                return True
    return False

# === AFTER: コードがそれ自体で語る ===

from dataclasses import dataclass

@dataclass
class User:
    status: str
    role: str
    suspended: bool

def has_access(user: User) -> bool:
    return user.role == "admin" \
       and user.status == "active" \
       and not user.suspended
