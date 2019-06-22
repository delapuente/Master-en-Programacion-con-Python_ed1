import logging


class SecurityMeasure:
    ...


def new_security_measure(*args, **kwargs):
    logging.warning('Nueva medida de seguridad')
    return SecurityMeasure(*args, **kwargs)
