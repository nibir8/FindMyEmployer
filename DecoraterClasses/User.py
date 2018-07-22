import abc, six


@six.add_metaclass(abc.ABCMeta)
class User():
    @abc.abstractmethod
    def plan_rules(self,givenCount):
        pass
