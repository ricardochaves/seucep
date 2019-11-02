from rest_framework.renderers import BaseRenderer
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

        xml = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <address>
              <addresses>{data['addresses']}</addresses>
              <state>{data['state']}</state>
              <complement>{data['complement']}</complement>
              <cep>{data['cep']}</cep>
              <neighborhood>{data['neighborhood']}</neighborhood>
              <city>{data['city']}</city>
              <abbreviation>{data['abbreviation']}</abbreviation>
              <address_type>{data['address_type']}</address_type>
            </address>"""

        return xml
