from pre_pull_baseimage import get_pyversion, pull_baseimage

def main():
    print("pythonファイルが保存されました。")
    version = get_pyversion.main()
    pull_baseimage.main(version)
    