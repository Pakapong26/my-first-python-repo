import subprocess
import sys


def run(command):
    result = subprocess.run(
        command,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.returncode


print("🚀 GitHub Easy Commit")
print("=" * 40)

message = input("📝 ใส่ข้อความ commit: ").strip()

if not message:
    print("❌ กรุณาใส่ข้อความ commit ก่อน")
    sys.exit(1)

# เช็คว่าอยู่ใน Git repo หรือไม่
check_repo = run(["git", "rev-parse", "--is-inside-work-tree"])
if check_repo != 0:
    print("❌ โฟลเดอร์นี้ยังไม่ใช่ Git repo")
    sys.exit(1)

# เช็คว่ามีไฟล์เปลี่ยนจริงไหม
status = subprocess.run(
    ["git", "status", "--porcelain"],
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True
).stdout.strip()

if not status:
    print("✅ ไม่มีไฟล์เปลี่ยนแปลง จึงไม่ต้อง commit")
    sys.exit(0)

print("\n📂 กำลัง git add .")
add_code = run(["git", "add", "."])

if add_code != 0:
    print("❌ git add ไม่สำเร็จ")
    sys.exit(1)

print("\n💾 กำลัง git commit")
commit_code = run(["git", "commit", "-m", message])

if commit_code != 0:
    print("❌ git commit ไม่สำเร็จ")
    sys.exit(1)

print("\n🌐 กำลัง git push")
push_code = run(["git", "push"])

if push_code == 0:
    print("\n🎉 สำเร็จ! commit และ push ขึ้น GitHub แล้ว")
else:
    print("\n⚠️ push ไม่สำเร็จ ให้เช็ค internet / login GitHub / remote")
    sys.exit(1)