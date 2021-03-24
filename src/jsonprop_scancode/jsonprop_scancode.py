from plugincode.post_scan import PostScanPlugin
from plugincode.post_scan import post_scan_impl
from commoncode.cliutils import PluggableCommandLineOption
from commoncode.cliutils import POST_SCAN_GROUP
import json


@post_scan_impl
class GetJSON(PostScanPlugin):
    """
    A ScanCode post-scan plugin that generate a JSON property file which is compatible with dxplatform.
    """

    options = [
        PluggableCommandLineOption(('--jsonprop',),
                                   is_flag=True, default=False,
                                   help='Generate a JSON property file compatible with dxplatform.',
                                   help_group=POST_SCAN_GROUP)
    ]

    def is_enabled(self, jsonprop, **kwargs):
        return jsonprop

    def process_codebase(self, codebase, jsonprop, **kwargs):
        """
        Get property file.
        """
        if not self.is_enabled(jsonprop):
            return

        """
        [{
            name: "email@...",
            category: "email",
            file: "../..",
            value: 1
        },
        ...
        ]
        """

        result = []

        for resource in codebase.walk():

            if hasattr(resource, 'emails'):
                for email in resource.emails:
                    result.append({
                        "name": email["email"],
                        "category": "email",
                        "file": resource.path,
                        "value": 1
                    })

            if hasattr(resource, 'urls'):
                for url in resource.urls:
                    result.append({
                        "name": url["url"],
                        "category": "url",
                        "file": resource.path,
                        "value": 1
                    })

            if hasattr(resource, 'copyrights'):
                for cp in resource.copyrights:
                    result.append({
                        "name": cp["value"],
                        "category": "copyright",
                        "file": resource.path,
                        "value": 1
                    })

            if hasattr(resource, 'licenses'):
                for license in resource.licenses:
                    result.append({
                        "name": license["license"],
                        "category": "license",
                        "file": resource.path,
                        "value": 1
                    })

        # for resource in codebase.walk():
        #     print(dir(resource))
        #     break

        result_json = json.dumps(result)

        with open("result.json", "w") as f:
            f.write(result_json)

        print(result_json)
