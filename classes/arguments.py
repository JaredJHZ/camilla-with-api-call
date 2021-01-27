import argparse


class Arguments(object):
    def __init__(self):
        """
        construct the argument parse
        """
        self.ap = argparse.ArgumentParser()


        self.create_argument("-c", "--confidence", "minimum probability to filter weak detections",
        type=float, default=0.5, required=False)

        self.create_argument("-t", "--threshold", "threshold when applying non-maxima suppression",
        type=float, default=0.3, required=False)

        self.args = self.get_args()

    def create_argument(self, tag, name, help_message, required = True, type=str, default=""):

        self.ap.add_argument(
            tag,
            name,
            type=type,
            default=default,
            required=required,
            help=help_message)


    def get_args(self):
        """
        parse the arguments
        """
        return vars(self.ap.parse_args())
