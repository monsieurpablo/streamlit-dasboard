import re
from pathlib import Path

import pandas as pd


def parse_md(md_file):

    markdown = Path(md_file).read_text()  # read markdown file

    re_topics = re.compile(r"^#\s", re.MULTILINE)  # multiline parameter
    re_header = re.compile(r"([^;]*?)\n")  # remember greedy mode
    re_subheader = re.compile(r"^##\s", re.MULTILINE)  # multiline parameter
    re_meta = re.compile(r'\[:(.*)\]: # "(.*)"', re.MULTILINE)  # read metadata
    re_speckle = re.compile(r'\[:"speckle_name"\]: # "(.*)"', re.MULTILINE)  # read metadata

    topics = re_topics.split(markdown)  # split on every header

    md_dict = {}

    for topic in topics:
        try:
            title = re_header.search(topic).group(1).strip()
            # topic = "\n".join(topic.split("\n")[1:]) # remove title
            paragraph = re_subheader.split(topic)
            

            for text in paragraph:
                metadata = dict(re_meta.findall(text))
                metadata['parent'] = title

                md_dict[metadata['speckle_name']] = {}
                md_dict[metadata['speckle_name']]['txt'] = text
                md_dict[metadata['speckle_name']]['header'] = title
                md_dict[metadata['speckle_name']]['meta'] = metadata
        except Exception as e:
            print(e)

    return md_dict


def dict2df(md_dict):
    df = pd.DataFrame.from_dict(md_dict, orient='index')
    # explode a columm of dictionaries into separate columns
    # https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas
    df = pd.concat([df.drop(['meta'], axis=1),
                   df['meta'].apply(pd.Series)], axis=1)
    return df


def md2df(markdown_file):
    md_dict = parse_md(markdown_file)
    df_markdown = dict2df(md_dict)
    # df_markdown.to_csv('df_markdown.csv')
    return(df_markdown)

