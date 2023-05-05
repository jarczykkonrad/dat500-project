from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol

class TabToPipeSeparator(MRJob):

    OUTPUT_PROTOCOL = RawValueProtocol

    def mapper(self, _, line):
        pipe_sep_line = line.replace('\t', '|')
        yield None, pipe_sep_line

if __name__ == '__main__':
    TabToPipeSeparator.run()
