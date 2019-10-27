from rest_framework.renderers import BaseRenderer


class PipedRenderer(BaseRenderer):
    media_type = "text/piped"
    format = "text"
    charset = "utf-8"
    ensure_ascii = False
    default_flow_style = False

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized PIPED.
        """

        return "|".join(("{}:{}".format(*i) for i in data.items()))
