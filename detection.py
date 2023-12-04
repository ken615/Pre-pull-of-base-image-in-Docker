"""
拡張子が.pyのファイルの変更（保存）を検知して、versionを取得する
"""
from pre_pull_baseimage import pre_pull_excution
import time
from watchdog.observers.polling import PollingObserver
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
        #print(event)
        self.__callback_handler(self.callback)


def watch(path, callback, extensions):
    event_handler = WatchdogHandler(callback, extensions)
    observer = PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    dir_to_watch = "."
    extensions = ["*.py"]
    watch(dir_to_watch, pre_pull_excution.main, extensions)