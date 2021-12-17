"""Visualizing attention scores of tokens as word-weighted heatmap PDF file
Author: Utkarsh Patel
"""

class Visualizer:
    """Wrapper for creating heatmaps for documents"""
    def __init__(self):
        self._header = r'''\documentclass[10pt,a4paper]{article}
\usepackage[left=1.00cm, right=1.00cm, top=1.00cm, bottom=2.00cm]{geometry}
\usepackage{color}
\usepackage{tcolorbox}
\usepackage{CJK}
\usepackage{adjustbox}
\tcbset{width=0.9\textwidth,boxrule=0pt,colback=red,arc=0pt,auto outer arc,left=0pt,right=0pt,boxsep=5pt}
\begin{document}
\begin{CJK*}{UTF8}{gbsn}''' + '\n\n'

        self._footer = r'''\end{CJK*}
\end{document}'''

    def visualize(self,
                  word_list,
                  attention_list,
                  label_list,
                  latex_file,
                  title,
                  batch_size=20,
                  color='blue'):
        """Routine to generate attention heatmaps for given texts
        ---------------------------------------------------------
        Input:
        :param word_list: list of texts (each text is a list of words)
        :param attention_list: scores for each word, dimension same as word_list
        :param label_list: label for each text
        :param latex_file: name of the latex file
        :param title: title of latex file
        :param batch_size: Number of comments in each batch
        :param color: color used for visualization, can be 'blue', 'red', 'green', etc.
        """
        word_list_processed = []
        for x in word_list:
            word_list_processed.append(self._clean_word(x))

        with open(latex_file, 'w', encoding='utf-8') as f:
            f.write(self._header)
            f.write('\\section{%s}\n\n' % title)

            n_examples = len(word_list)
            n_batches = n_examples // batch_size

            for i in range(n_batches):
                batch_word_list = word_list_processed[i * batch_size: (i + 1) * batch_size]
                batch_attention_list = attention_list[i * batch_size: (i + 1) * batch_size]
                batch_label_list = label_list[i * batch_size: (i + 1) * batch_size]
                f.write('\\subsection{Batch %d}\n\n' % (i + 1))
                for j in range(batch_size):
                    f.write('\\subsubsection{Comment %d - %s}\n\n' % (j + 1, batch_label_list[j]))
                    sentence = batch_word_list[j]
                    score = batch_attention_list[j]
                    assert len(sentence) == len(score)
                    f.write('\\noindent')
                    for k in range(len(sentence)):
                        f.write('\\colorbox{%s!%s}{' % (color, score[k]) + '\\strut ' + sentence[k] + '} ')
                    f.write('\n\n')

            f.write(self._footer)

    @staticmethod
    def _clean_word(word_list):
        new_word_list = []
        for word in word_list:
            for latex_sensitive in ["\\", "%", "&", "^", "#", "_", "{", "}"]:
                if latex_sensitive in word:
                    word = word.replace(latex_sensitive, '\\' + latex_sensitive)
            new_word_list.append(word)
        return new_word_list

if __name__ == '__main__':
    viz = Visualizer()
    word_list = [['This', 'script', 'generates', 'heatmaps'], ['Change', 'this', 'to', 'try', 'the', 'visualizer']]
    attention_list = [[0, 70, 0, 80], [0, 50, 0, 0, 0, 70]]
    label_list = ['Description', 'Experiment']
    viz.visualize(word_list, attention_list, label_list,
                  latex_file='sample.tex',
                  title='Generating heatmaps',
                  batch_size=len(word_list),
                  color='blue')
    # Copy the content of sample.tex on overleaf and compile to view the heatmap
