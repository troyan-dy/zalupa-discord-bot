from logging import Logger

import loguru


class LoggerMixin:
    @property
    def logger(self) -> Logger:
        if not hasattr(self, "_logger"):
            self._logger = loguru.logger.bind(class_name=self.__class__.__name__)

        return self._logger
