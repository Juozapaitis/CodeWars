import random
def get_featured_projects(all_projects):
    featured_projects = []
    popular_projects = []
    just_projects = []
    if len(all_projects) <= 10:
        featured_projects = all_projects
    else:
        for i in range(len(all_projects)):
            if all_projects[i]['nreceiving_from'] > 5:
                popular_projects.append(all_projects[i])
            else:
                just_projects.append(all_projects[i])
        if len(popular_projects) >= 7:
            featured_projects += random.sample(popular_projects, 7)
        elif len(popular_projects) < 7 and len(popular_projects) != 0:
            featured_projects += popular_projects
        else:
            if len(just_projects) >= 10:
                featured_projects += random.sample(just_projects, 10)
                just_projects = []
            else:
                featured_projects += just_projects
                just_projects = []
        while len(featured_projects) < 10 and len(just_projects) > 0:
            featured_projects.append(just_projects[0])
            just_projects.pop(0)
    random.shuffle(featured_projects)
    return featured_projects