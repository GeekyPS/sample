from data import company_testimonials


ans = 0
for part in company_testimonials:
    try:
        comp = part['company']
        web = part['web_url']
        web = len(web)

        print(f'For company {comp} number is: {web})')
        ans+= web
    except Exception as e:
        print(e)
        pass

print(ans)


"""
Done for company Barclays
Done for company Aviva
Done for company Lloyds Banking Group
Done for company Lloyds Banking Group
Done for company Standered Chartered
Done for company Prudentials
Done for company Aviva
Done for company HSBC
Done for company Standered Chartered
Done for company Aviva
Done for company Legal and General
Done for company Legal and General
Done for company Barclays
Done for company Standered Chartered
Done for company Prudentials
Done for company Natwest
Done for company Zurich
Done for company Lloyds Banking Group
Done for company HSBC
Done for company Zurich
Done for company Prudentials
Done for company Aviva
Done for company AXA UK
Done for company Legal and General
Done for company AXA UK
Done for company Aviva
Done for company Legal and General
Done for company Legal and General
Done for company AXA UK
Done for company Atos
Done for company Zurich
Done for company Atos
Done for company AXA UK
Done for company Atos
Done for company Legal and General
Done for company AXA UK
Done for company Atos
Done for company Savills
Done for company Zurich
Done for company General
Done for company General
Done for company AXA UK
Done for company Savills
Done for company Atos
Done for company Vodafone
Done for company Vodafone
Done for company BAE System
Done for company BAE System
Done for company BAE System
Done for company Savills
Done for company Vodafone
Done for company Capita
Done for company Savills
Done for company Linklaters
Done for company Landsec
Done for company General
Done for company Herbert Smith Freehills
Done for company Vodafone
Done for company Zurich
Done for company BT Group
Done for company Freshfields Bruckhaus Deringer
Done for company Microsoft UK
Done for company Vodafone
Done for company Boston Consulting Group
Done for company BT Group
Done for company ARM Holdings
Done for company Linklaters
Done for company Norton Rose Fulbright
Done for company Norton Rose Fulbright
Done for company Pinsent Masons
Done for company Vodafone
Done for company Slaughter and May
Done for company Capgemini
Done for company Jones Lang LaSalle
Done for company Barratt Developments
Done for company Pinsent Masons
Done for company Pinsent Masons
Done for company Freshfields Bruckhaus Deringer
Done for company Barratt Developments
Done for company Care UK
Done for company Cushman & Wakefield
Done for company Cygnet Health Care
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company British Land
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Fujitsu UK
Done for company Taylor Wimpey
Done for company Fujitsu UK
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Environment Agency 
Done for company Taylor Wimpey
Done for company Department for Work and Pensions (DWP)
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Barratt Developments
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Cygnet Health Care
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Bupa
Done for company Bupa
Done for company Department for Education (DfE)
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Taylor Wimpey
Done for company Care UK
Done for company Allen & Overy
Done for company Barratt Developments
Done for company PricewaterhouseCoopers
Done for company Deloitte
Done for company Taylor Wimpey
Done for company PricewaterhouseCoopers
Done for company Nation Health Service(NHS)
Done for company HM Revenue and Customs (HMRC)
Done for company PricewaterhouseCoopers
Done for company Bupa
Done for company Ernst & Young
Done for company HM Revenue and Customs (HMRC)
Done for company Deloitte
Done for company Ernst & Young
Done for company Deloitte
Done for company KPMG
Done for company Ministry of Defence (MoD)
Done for company KPMG
Done for company KPMG
Done for company HM Revenue and Customs (HMRC)
Done for company Accenture
Done for company Ernst & Young
Done for company Accenture
Done for company Ernst & Young
Done for company KPMG
Done for company Grant Thornton UK LLP
Done for company Grant Thornton UK LLP
Done for company McKinsey & Company
Done for company McKinsey & Company
Done for company McKinsey & Company
Done for company Ernst & Young
Done for company DLA Piper
Done for company Home Office
Done for company Grant Thornton UK LLP
Done for company DLA Piper
Done for company KPMG
Done for company DLA Piper
Done for company Accenture
Done for company DLA Piper
Done for company Balfour Beatty
Done for company Met Office
Done for company Balfour Beatty
Done for company Met Office
Done for company HC-One
Done for company DLA Piper
Done for company HC-One
Done for company Home Office
Done for company Home Office
Done for company Eversheds Sutherland
Done for company HC-One
Done for company Eversheds Sutherland
Done for company Balfour Beatty
Done for company HC-One
Done for company Eversheds Sutherland
Done for company Eversheds Sutherland
Done for company Eversheds Sutherland
Done for company Eversheds Sutherland
Done for company HC-One
Done for company Eversheds Sutherland
Done for company Eversheds Sutherland
Done for company Four Seasons Health Care
Done for company Eversheds Sutherland
Done for company Eversheds Sutherland
Done for company Four Seasons Health Care
Done for company Four Seasons Health Care
Done for company NHS
Done for company Four Seasons Health Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company NHS
Done for company Virgin Care
Done for company Virgin Care
Done for company Home Office
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company NHS
Done for company Home Office
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Clifford Chance
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care
Done for company Virgin Care


"""