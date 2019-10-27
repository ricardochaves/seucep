from rest_framework.renderers import BaseRenderer
from seucep.apps.drf.renders.xml.parser import dict2xml
from seucep.apps.drf.renders.yaml.encode import SafeDumper


class XmlRenderer(BaseRenderer):
    media_type = "application/xml"
    format = "xml"
    encoder = SafeDumper

    charset = "utf-8"
    ensure_ascii = False
    default_flow_style = False

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """

        return dict2xml(data, root_node="Address")
