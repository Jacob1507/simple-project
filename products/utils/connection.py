from typing import Optional, Any

import mongoengine


class Connection:
    def __init__(self, db: str, alias: Optional = None):
        self.db = db
        self.alias = alias

    def simple_connection(self, func) -> Any:
        """Simple connection, don't require authentication"""
        mongoengine.connect(db=self.db, alias=self.alias)

        def wrapper_func(*args, **kwargs):
            func(*args, **kwargs)

        return func

    def disconnect(self) -> None:
        if self.alias:
            mongoengine.disconnect(alias=self.alias)
        mongoengine.disconnect()
