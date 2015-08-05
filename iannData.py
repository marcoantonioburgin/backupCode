from __future__ import print_function
import pysolr
import re

# Query Iann.pro
iannData = pysolr.Solr('http://iann.pro/solr/', timeout=20)

resultsIann = iannData.search(q='*:*', rows='10', fq='start:[2015-01-01T00:00:00Z TO *]')

#resultsIann = iannData.search(q='*:*', rows='5000', fq='start:[2015-01-01T00:00:00Z TO *]')


# Solr LocalHost
solrLocal = pysolr.Solr('http://localhost:8983/solr/eventsData', timeout=10)
resultsLocal = solrLocal.search(q='*:*', rows='5000')

for result in resultsIann:

    listFull = []

    title = format(result['title'])

    start = format(result['start'])

    end = format(result['end'])

    city = format(result['city'])

    country = format(result['country'])

    provider = format(result['provider'])

    link = format(result['link'])

    field = format(result['field'])

    strText = field.replace("[u'", "")

    strClear = strText.replace("']", "")

    if re.search("', u'", strClear):

        array = strClear.split("', u'")

        for index in array:
            strEach = index
            listFull.append(strEach)

    else:

        listFull.append(strClear)

    solrLocal.add([
        {
            "title": title,
            "start": start,
            "end": end,
            "city": city,
            "country": country,
            "field": listFull,
            "provider": provider,
            "link": link
        }
    ])


#solrLocal.delete(q='*:*')


# Print all the infos
'''
for result in resultsLocal:

    print("field: " + field)
    print (type(field))
    print(" ")
'''
'''
    title = format(result['title'])
    print("Title: " + title)

    dateStart = format(result['dateStart'])
    print("Start: " + dateStart)

    dateEnd = format(result['dateEnd'])
    print("End: " + dateEnd)

    city = format(result['city'])
    print("City: " + city)

    country = format(result['country'])
    print("Country: " + country)

    print(" ")
'''
