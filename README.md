# ScanCode-Plugin

## About

This is a **ScanCode post-scan plugin** that generate a JSON property file, different from the default options, which is also compatible with dxplatform. \
It is written in Python and does not work on its own, meaning it needs to have scancode-toolkit installed.

## Before Installing

ScanCode requires either **Python** 3.6.x and is tested on Linux, Mac, and Windows.
Make sure Python 3.6 is installed first. Also keep in mind that this plugin was written for the latest release and it may not work on previous ones.

## Installation

**1. Install scancode-toolkit**

```
git clone https://github.com/nexB/scancode-toolkit.git
cd scancode-toolkit
pip install scancode-toolkit
```

For further information you can also read [ScanCode's documentation](https://scancode-toolkit.readthedocs.io/).

**2. Install the plugin**

First you need to clone the project via Git:

```
git clone https://github.com/TeamFrost/scancode-plugin.git
```

After you should go to the the folder of **scancode-toolkit** and make a folder named "plugins", the path should look like this:

```
scancode-toolkit/plugins/
```

Next copy the folder that contains the plugin here. If you made all the steps right the path should look like this:

```
scancode-toolkit/plugins/scancode-plugin/
```

The last step represents loading the plugin by opening a terminal/command prompt and running:

```
pip install .
```

## Usage

To run scancode you should open a terminal/command prompt in its root directory and you can start with the help command to see all the options you have.

```
scancode --help
```

If you installed our plugin correctly it should appear under the **post-scan** section with the command:

```
--jsonprop
```

To run your first scan you can try:

```
scancode -cplue <path to the directory you want to scan> --jsonprop --json-pp <path to the output file>
```

The first _-cplue_ instructs scancode to look for copyrights, packages, licenses, urls and email. After, our custom command for the plugin _--jsonprop_ generates a **result.json** file in the root directory of scancode. The file is not formatted and you should use an online converter to a prettier JSON if you want to better understand it. The files contains the following information:

| name                           | category  | path             | value |
| ------------------------------ | --------- | ---------------- | ----- |
| string of the actual **email** | email     | path to the file | 1     |
| string of the actual **url**   | url       | path to the file | 1     |
| value of the **copyright**     | copyright | path to the file | 1     |
| name of the **license**        | license   | path to the file | 1     |
| name of the **package**        | package   | path to the file | 1     |

The path is without the root folder for purpose of integration with dxplatform. Also, likewise, the existence of the value field is motivated by the wanted integration.

Lastly, to see the results provided by scancode you should open the file that you included in the command. Moreover, if you want this results to be seen in the terminal / command prompt you can replace _<path to the output file>_ with _-_.

## Screenshots

## Thanks

This plugin would not be possible without [nexB/scancode-toolkit](https://github.com/nexB/scancode-toolkit), so we would like to thank them for their work and be sure to also check them out.

## License

[Apache-2.0 License](LICENSE)
