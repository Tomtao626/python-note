dict_a = {
	'A': ['WodAndFit，MyPersonalize，MercedesArtBoutique，LinenDuet，PersonalisedGADGETS'],
	'B': ['soletgo，DEMAIOShop，SbrnFinds，HolidayApparel'],
	'C': ['PrinteesPlus，OhMyDesignsbyJax，DaniCovers，CaseSpaceDesign，Love2MakeIt，RusticRouteDesigns，TheAestheticKnot，byzoecharlotte，SunkissedDesignsCA']
}
list_1 = ['PrinteesPlus', 'WodAndFit', 'soletgo', 'SbrnFinds', 'DaniCovers', 'SunkissedDesignsCA', 'HolidayApparel']

dict_b = dict()
for k in dict_a: dict_b.update({f'{k}': len(list(set(list_1).intersection(dict_a[k][0].split('，'))))})
print(dict_b)
