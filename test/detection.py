"""
拡張子が.pyのファイルの変更（保存）を検知して、versionを取得する
"""
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class WatchdogHandler(PatternMatchingEventHandler):
    """
    PatternMatchingEventHandlerクラスを実装したクラス
    """

    def __init__(self, callback, patterns):
        """
        コンストラクタ

        Args:
            callback (function) : 監視中に、特定のイベントが発生した場合に起こすイベント
            patterns (list[str]) : 監視する対象の拡張子

        Returns:
            void
        """
        super(WatchdogHandler, self).__init__(patterns=patterns)
        self.callback = callback

    def __callback_handler(self, func,*args):
        return func(*args)

    def on_modified(self, event):
        print(event)
        self.__callback_handler(self.callback)


def watch(path, callback, extensions):
    event_handler = WatchdogHandler(callback, extensions)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def say_hello():
    print("pythonファイルが保存されました。")
    version = get_pyversion()
    print(f"version : {version}")


def get_pyversion():
    cmd = "python -V"
    process = (subprocess.Popen(cmd, 
                                stdout=subprocess.PIPE,
                                shell=True).communicate()[0]).decode('utf-8')
    return process


if __name__ == "__main__":
    dir_to_watch = ".."
    extensions = ["*.py"]
    watch(dir_to_watch, say_hello, extensions)