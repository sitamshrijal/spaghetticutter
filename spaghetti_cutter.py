import datetime
import os
import random

from moviepy.editor import VideoFileClip
from texttable import Texttable

# the extension of the video file
FILE_EXTENSION = '.mov'


def main():
    # Enter folder name with video files.
    location = input('Directory path: ')

    # length of new video in s
    length = int(input('Length of sequence (in s): '))

    video_files = []
    file_names = []
    print("\nOutput written to output.txt")

    f = open("output.txt", "w")

    table = Texttable()
    table.add_row(["Clip Position", "Clip Name", "Start Point", "End Point", "Total Duration"])

    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(FILE_EXTENSION):
                video_files.append(os.path.join(root, file))
                file_names.append(file)

    count = 0
    while length > 0:
        file = random.choice(video_files)

        index = video_files.index(file)

        if file.endswith(FILE_EXTENSION):
            # Video length
            clip = VideoFileClip(file)

            frame_rate = clip.fps

            # random frame
            start_frame = random.randint(1, int(frame_rate))
            end_frame = random.randint(1, int(frame_rate))

            # Start timestamp of clip
            a = random.uniform(0, clip.duration)
            b = random.uniform(0, clip.duration)

            start = 0
            end = 0

            if a < b:
                start = a
                end = b
            else:
                end = a
                end = b

            duration = end - start

            start_string = f'{datetime.timedelta(seconds=round(start))}:{start_frame}'
            end_string = f'{datetime.timedelta(seconds=round(end))}:{end_frame}'

            table.add_row([count + 1, file_names[index],
                           start_string,
                           end_string,
                           datetime.timedelta(seconds=round(duration))])
            count += 1

            length -= duration

    print(file_names)
    f.write(table.draw())


if __name__ == '__main__':
    main()
