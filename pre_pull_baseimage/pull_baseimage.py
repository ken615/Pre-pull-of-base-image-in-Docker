import os

def main(version):
    print(f"python:{version}-bookwormイメージをpullします。")
    os.system(f"docker image pull python:{version}-bookworm")
    print(f"python:{version}-bookwormイメージのpullが完了しました。")

    return