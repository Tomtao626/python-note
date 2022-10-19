import ujson


def read_json(filepath):
	with open(filepath, 'r', encoding='utf-8') as fr:
		codejson = ujson.load(fr)
	return codejson


areacode_list = ["+93", "+355", "+213", "+376", "+244", "+1264", "+1268", "+54", "+374", "+297", "+61", "+43",
                 "+994", "+1242", "+973", "+880", "+1246", "+375", "+32", "+501", "+229", "+1441", "+975", "+591",
                 "+387", "+267", "+55", "+673", "+359", "+226", "+257", "+855", "+237", "+1", "+238", "+1345",
                 "+236", "+235", "+56", "+86", "+57", "+269", "+682", "+506", "+385", "+357", "+420", "+242", "+45",
                 "+253", "+1767", "+1809", "+670", "+593", "+20", "+503", "+240", "+372", "+251", "+298", "+679",
                 "+358", "+33", "+594", "+241", "+220", "+995", "+49", "+233", "+350", "+30", "+299", "+1473",
                 "+590", "+1671", "+502", "+224", "+245", "+592", "+509", "+504", "+852", "+36", "+354", "+91",
                 "+62", "+964", "+353", "+972", "+39", "+225", "+1876", "+81", "+962", "+76", "+254", "+686",
                 "+965", "+996", "+856", "+371", "+961", "+266", "+231", "+218", "+423", "+370", "+352", "+853",
                 "+389", "+261", "+265", "+60", "+960", "+223", "+356", "+596", "+222", "+230", "+52", "+373",
                 "+377", "+976", "+382", "+1664", "+212", "+258", "+95", "+264", "+977", "+31", "+687", "+64",
                 "+505", "+227", "+234", "+47", "+968", "+92", "+680", "+930", "+507", "+675", "+595", "+51", "+63",
                 "+48", "+351", "+1787", "+974", "+262", "+40", "+7", "+250", "+1869", "+1758", "+1784", "+685",
                 "+239", "+966", "+221", "+381", "+248", "+232", "+65", "+421", "+386", "+677", "+252", "+27",
                 "+82", "+211", "+34", "+94", "+597", "+268", "+46", "+41", "+886", "+992", "+255", "+66", "+228",
                 "+676", "+2908", "+216", "+90", "+993", "+1649", "+256", "+380", "+971", "+44", "+598", "+998",
                 "+678", "+58", "+84", "+1284", "+1340", "+967", "+260", "+850", "+1829", "+1849", "+599", "+1939",
                 "+1868", "+263", "+970"]
code_list = read_json("aws_sms_price.json")
sdict = {}
for i in code_list:
	if i['areacode'] == None:
		print(i['areacode'])
		continue
	s = {"price": round(i['price'] * 6.3872, 4)}
	sdict.update({f"{i['areacode']}": s})

print(ujson.dumps(sdict))
