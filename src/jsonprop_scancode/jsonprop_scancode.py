from plugincode.post_scan import PostScanPlugin
from plugincode.post_scan import post_scan_impl
from commoncode.cliutils import PluggableCommandLineOption
from commoncode.cliutils import POST_SCAN_GROUP


@post_scan_impl
class GetJSON(PostScanPlugin):
    """
    A ScanCode post-scan plugin that generate a JSON property file which is compatible with dxplatform.
    """

    options = [
        PluggableCommandLineOption(('--jsonprop',),
                                   is_flag=True, default=False,
                                   help='Generate a simple "Hello ScanCode" greeting in the terminal.',
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

        print("Property File!")
