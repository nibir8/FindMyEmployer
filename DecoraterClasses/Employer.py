import abc, six


@six.add_metaclass(abc.ABCMeta)
class Employer:
    @abc.abstractmethod
    def plan_rules(self,givenCount,userCount,messagePermission):
        pass
