import abc, six


@six.add_metaclass(abc.ABCMeta)
class Employee:
    @abc.abstractmethod
    def plan_rules(self,givenCount,userCount,messagePermission):
        pass
