labels = ["A", "B", "C", "D"]

def mctest_format(tsv_file, ans_file):
	with open(tsv_file) as tsv_data:
		tsv_lines = tsv_data.readlines()
	with open(ans_file) as ans_data:
		ans_lines = ans_data.readlines()

	corpus = []
	for tsv, ans in zip(tsv_lines, ans_lines):
		corpus.append(parse_mctest_instance(tsv, ans))
	return corpus

def parse_mctest_instance(tsv_chunk, ans_chunk):
	tsv_tabs = tsv_chunk.strip().split('\t')
	ans_tabs = ans_chunk.strip().split('\t')

	id = tsv_tabs[0]
	ann = tsv_tabs[1]
	passage = tsv_tabs[2]

	# the dictionary for populating a set of passage/questions/answers
	qset_dict = {}
	qset_dict['passage'] = passage

	# collect questions / answers
	qset_dict['questions'] = parse_mctest_questions(tsv_tabs[3:], ans_tabs)

	return {'question-set' : qset_dict}

def parse_mctest_questions(question_list, ans_tabs):
	questions = []
	for i in range(0, len(question_list), 5):
		qdict = {}
		# parse answers
		answers = []
		correct_answer = ans_tabs[int(i / 5)]
		for j in range(1,5):
			label = labels[j-1]
			answer = {
				'label' : label,
				'correct' : label == correct_answer,
				'text' : question_list[i+j]
			}
			answers.append(answer)

		# parse question
		qcols = question_list[i].split(':')
		qdict['question'] = {
			'question-type' : qcols[0],
			'text' : qcols[1],
			'answer-candidates' : answers
		}
		questions.append(qdict)
	return questions
