from ariadne.types import ExtensionSync


class ResolveBatcher(ExtensionSync):

    def resolve(self, next_, parent, info, **kwargs):
        print("RESOLVE HOOK CALLED:\nnext: {}\nparent: {}\nInfo:{}".format(
            next_, parent, info))
        return next_(parent, info)
