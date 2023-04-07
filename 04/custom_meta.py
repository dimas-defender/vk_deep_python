class CustomMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        keys_to_change = []
        for key in classdict:
            if key.startswith('__') and key.endswith('__'):
                continue
            keys_to_change.append(key)

        for key in keys_to_change:
            classdict['custom_' + key] = classdict.pop(key)

        cls = super().__new__(mcs, name, bases, classdict, **kwargs)
        setattr(cls, '__setattr__', mcs.__setattr__)
        return cls

    def __setattr__(cls, name, val):
        if not (name.startswith('__') and name.endswith('__')):
            name = 'custom_' + name
        return super(type(cls), cls).__setattr__(name, val)
