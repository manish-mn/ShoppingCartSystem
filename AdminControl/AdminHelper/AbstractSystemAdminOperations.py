from abc import ABC, abstractmethod


class AbstractSystemAdminOperations(ABC):
    @abstractmethod
    def verify_admin_list(self):
        pass

    @abstractmethod
    def verify_admin_credentials_and_log_in(self, user_name, password):
        pass

    @abstractmethod
    def add_admin(self):
        pass
