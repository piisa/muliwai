
def collapse_ner(docs, ner_key, collapse_ner_key, text_key, stopwords, do_cleanup_only=False):
    #print ("collapse_ner")
    for doc in docs.values():
      text = doc.get(text_key, "")

      if True:
        #do some cleanups. we don't want any ner that are just short numbers (but what about govt id?), stopwords or single characters.
          ner =  doc[ner_key]
          for key in list(doc[ner_key].keys()):
            ner_word = key[0]
            try:
              if len(ner_word) < 4 and float(ner_word):
                #print ("deleting ", ner_word)
                del doc[ner_key][key]
                continue
            except:
              pass
            if ner_word.lower() in stopwords or (not cjk_detect(ner_word) and len(ner_word) <= 1):
              #print ("deleting ", ner_word)
              del doc[ner_key][key]

      if do_cleanup_only:
        continue
      #TODO - generalize long ner to rest of the sentences if not already tagged

      chunk2ner = doc.get(ner_key, {})
      chunks = list(chunk2ner.items())
      chunks.sort(key=lambda a: a[0][1]+(1.0/(1.0+a[0][2]-a[0][1])))
      chunks2 = []

      for mention, labelsHash in chunks:
        mention = list(mention)
        if not chunks2:
          chunks2.append([mention[0], mention[1], mention[2], labelsHash])
        # completely or mostly subsumed
        elif chunks2[-1][2] >= mention[2] or chunks2[-1][2] - mention[1] > 3:
          prev_ent, prev_start, prev_end, prev_labelsHash = chunks2[-1]
          for tag in labelsHash:
            prev_labelsHash[tag]  = prev_labelsHash.get(tag, 0) + labelsHash.get(tag, 0)
          chunks2[-1][2] = mention[2]
          #print (chunks2[-1], text)
          chunks2[-1][0] = text[chunks2[-1][1]:chunks2[-1][2]]
        elif chunks2[-1][2] < mention[1]:
          chunks2.append([mention[0], mention[1], mention[2], labelsHash])
        # partially subsumed
        else:
          if mention[2] - mention[1] > chunks2[-1][2] - chunks2[-1][1]:
              chunks2[-1][2] = mention[1] -1
              chunks2[-1][0] = text[chunks2[-1][1]:chunks2[-1][2]]
          else:
              mention[1] = chunks2[-1][2] + 1
              mention[0] = text[mention[1]:mention[2]]
          chunks2.append([mention[0], mention[1], mention[2], labelsHash])

      ner = {}
      for ent, start, end, labelsHash in chunks2:
        ent = ent.strip(strip_chars)
        if ent:
          mention = (ent, start, start + len(ent))
          labelsHash2 = {}
          for key, val in labelsHash.items():
            if type(key) is tuple:
              key = key[0]
            labelsHash2[key] = labelsHash2.get(key, 0) + val
          #do hypo collapse so that loc->address, person->public_figure when there are overlaps, date/id->date
          if 'PERSON' in labelsHash2 and 'PUBLIC_FIGURE' in labelsHash2:
            labelsHash2['PUBLIC_FIGURE'] = labelsHash2['PUBLIC_FIGURE'] + labelsHash2['PERSON']
            del labelsHash2['PERSON']
          if 'LOC' in labelsHash2 and 'ADDRESS' in labelsHash2:
            labelsHash2['ADDRESS'] = labelsHash2['ADDRESS'] + labelsHash2['LOC']
            del labelsHash2['LOC']
          if 'DATE' in labelsHash2 and 'AGE' in labelsHash2:
            labelsHash2['AGE'] = labelsHash2['AGE'] + labelsHash2['DATE']
            del labelsHash2['DATE']
          if 'DATE' in labelsHash2 and 'ID' in labelsHash2:
            del labelsHash2['ID'] # we prefe dates to ids?
          if 'CARDINAL' in labelsHash2 and 'ID' in labelsHash2:
            labelsHash2['ID'] = labelsHash2['ID'] + labelsHash2['CARDINAL']
            del labelsHash2['CARDINAL']

          ner[mention] = labelsHash2
      doc[collapse_ner_key] = ner


    return docs
