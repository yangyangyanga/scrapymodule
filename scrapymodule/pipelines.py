# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapymodule.insert_mysql import InsertMysql

class BristolMasterSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, degree_type, start_date, " \
              "overview, duration, modules, career, deadline, tuition_fee, location, Rntry_requirements, IELTS, " \
              "URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s) on duplicate key update university=VALUES(university), department=VALUES(department), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),start_date=VALUES(start_date), " \
              "overview=VALUES(overview),duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), " \
              "deadline=VALUES(deadline), tuition_fee=VALUES(tuition_fee), location=VALUES(location)," \
              "Rntry_requirements=VALUES(Rntry_requirements), IELTS=VALUES(IELTS), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['department'], item['programme'], item['degree_type'], item['start_date'],
                                      item['overview'], item['duration'], item['modules'], item['career'], item['deadline'],
                                      item['tuition_fee'], item['location'], item['Rntry_requirements'], item['IELTS'], item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class StrathMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, programme, degree_type, start_date, " \
              "overview, type,duration,  modules, teaching_assessment, career, deadline, tuition_fee, Rntry_requirements, IELTS, " \
              "other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s) on duplicate key update university=VALUES(university), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),start_date=VALUES(start_date), " \
              "overview=VALUES(overview),type=VALUES(type),duration=VALUES(duration), modules=VALUES(modules), teaching_assessment=VALUES(teaching_assessment),career=VALUES(career), " \
              "deadline=VALUES(deadline), tuition_fee=VALUES(tuition_fee), " \
              "Rntry_requirements=VALUES(Rntry_requirements), IELTS=VALUES(IELTS),other=VALUES(other), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['programme'], item['degree_type'], item['start_date'],
                                      item['overview'], item['type'], item['duration'], item['modules'], item['teaching_assessment'], item['career'], item['deadline'],
                                      item['tuition_fee'], item['Rntry_requirements'], item['IELTS'], item['other'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class ManchesterMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, programme, degree_type, " \
              "overview, type, duration, modules,  career, tuition_fee, IELTS,interview, how_to_apply," \
              "entry_requirements, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s) on duplicate key update university=VALUES(university), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type), " \
              "overview=VALUES(overview),type=VALUES(type),duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), " \
              "tuition_fee=VALUES(tuition_fee), " \
              "IELTS=VALUES(IELTS),interview=VALUES(interview),how_to_apply=VALUES(how_to_apply),entry_requirements=VALUES(entry_requirements),other=VALUES(other), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['programme'], item['degree_type'],
                                      item['overview'],  item['type'],item['duration'], item['modules'], item['career'],
                                      item['tuition_fee'],item['IELTS'], item['interview'],item['how_to_apply'],item['entry_requirements'],item['other'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class KingsMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university,department, programme, degree_type, " \
              "overview, mode, duration, modules,  career, deadline, application_fee, tuition_fee," \
              "Rntry_requirements, average_score, IELTS, application_documents, " \
              "entry_requirements, URL) values( %s, %s, %s,  %s, %s, %s, %s, %s, %s,  %s, %s, %s," \
              "%s, %s, %s, %s,  %s, %s) on duplicate key update university=VALUES(university), department=VALUES(department), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),overview=VALUES(overview)," \
              "mode=VALUES(mode), duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), deadline=VALUES(deadline)," \
              "application_fee=VALUES(application_fee),tuition_fee=VALUES(tuition_fee),Rntry_requirements=VALUES(Rntry_requirements), " \
              "average_score=VALUES(average_score)," \
              "IELTS=VALUES(IELTS),application_documents=VALUES(application_documents)," \
              "entry_requirements=VALUES(entry_requirements), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['department'], item['programme'], item['degree_type'],
                                      item['overview'],  item['mode'],item['duration'], item['modules'], item['career'],item['deadline'], item['application_fee'],
                                      item['tuition_fee'],item['Rntry_requirements'],item['average_score'],item['IELTS'],
                                     item['application_documents'],item['entry_requirements'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class ManchesterMastersResearchSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class StrathMastersResearchSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class AstonMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

# 数据库表结构增加了字段
class SalfordBenSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/salfordBenSchoolMysqlerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class SalfordMastersTaughtSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/salfordBenSchoolMysqlerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class SalfordMastersResearchSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class CardiffmetBenSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class CardiffMastersTaughtSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class HertsBenSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class BathspaBenSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class UclanBenSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class HopeMastersTaughtSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class SchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, entry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, url,tegree_type, degree_level) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "entry_requirements =VALUES(entry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), url =VALUES(url),tegree_type =VALUES(tegree_type),degree_level =VALUES(degree_level)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["entry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["url"], item["tegree_type"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

# 2018/02/08 修改表tmp_shool_major
class School1Pipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into tmp_school_major(university, country, city, website, department, programme, degree_level, " \
              "degree_type, ucas_code, mode, application_date, deadline, start_date, degree_description, " \
              "overview, duration, modules, application_fee, tuition_fee, teaching, assessment, career, location, " \
              "entry_requirements, chinese_requirements, ATAS, GPA, average_score, accredited_university, Alevel, " \
              "IB, IELTS, IELTS_L, IELTS_S, IELTS_R, IELTS_W, TOEFL, TOEFL_L, TOEFL_S, TOEFL_R, TOEFL_W, GRE, GMAT," \
              " LSAT, MCAT, working_experience, interview, portfolio, application_documents, how_to_apply, school_test, " \
              "SATI, SATII, SAT_code, ACT, ACT_code, other, url) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (item["university"], item["country"], item["city"], item["website"],
                                      item["department"], item["programme"], item["degree_level"], item["degree_type"],
                                      item["ucas_code"], item["mode"], item["application_date"], item["deadline"],
                                      item["start_date"], item["degree_description"], item["overview"], item["duration"],
                                      item["modules"], item["application_fee"], item["tuition_fee"], item["teaching"],
                                      item["assessment"], item["career"], item["location"], item["entry_requirements"],
                                      item["chinese_requirements"], item["ATAS"], item["GPA"], item["average_score"],
                                      item["accredited_university"], item["Alevel"], item["IB"], item["IELTS"],
                                      item["IELTS_L"], item["IELTS_S"], item["IELTS_R"], item["IELTS_W"], item["TOEFL"],
                                      item["TOEFL_L"], item["TOEFL_S"], item["TOEFL_R"], item["TOEFL_W"], item["GRE"],
                                      item["GMAT"], item["LSAT"], item["MCAT"], item["working_experience"],
                                      item["interview"], item["portfolio"], item["application_documents"],
                                      item["how_to_apply"], item["school_test"], item["SATI"], item["SATII"],
                                      item["SAT_code"], item["ACT"], item["ACT_code"], item["other"], item["url"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

class School1UpdatePipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "update tmp_school_major set entry_requirements = %s where university = %s and programme = %s and degree_level = %s"
        try:
            self.cursor.execute(sql, (item["entry_requirements"],item["university"], item["programme"], item["degree_level"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        # self.close()
        return item

# 自己本地的数据库
class SchoolPipelineLocal(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into tmp_school_major_copy(university, country, city, website, department, programme, degree_level, " \
              "degree_type, ucas_code, mode, application_date, deadline, start_date, degree_description, " \
              "overview, duration, modules, application_fee, tuition_fee, teaching, assessment, career, location, " \
              "entry_requirements, chinese_requirements, ATAS, GPA, average_score, accredited_university, Alevel, " \
              "IB, IELTS, IELTS_L, IELTS_S, IELTS_R, IELTS_W, TOEFL, TOEFL_L, TOEFL_S, TOEFL_R, TOEFL_W, GRE, GMAT," \
              " LSAT, MCAT, working_experience, interview, portfolio, application_documents, how_to_apply, school_test, " \
              "SATI, SATII, SAT_code, ACT, ACT_code, other, url) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (item["university"], item["country"], item["city"], item["website"],
                                      item["department"], item["programme"], item["degree_level"], item["degree_type"],
                                      item["ucas_code"], item["mode"], item["application_date"], item["deadline"],
                                      item["start_date"], item["degree_description"], item["overview"], item["duration"],
                                      item["modules"], item["application_fee"], item["tuition_fee"], item["teaching"],
                                      item["assessment"], item["career"], item["location"], item["entry_requirements"],
                                      item["chinese_requirements"], item["ATAS"], item["GPA"], item["average_score"],
                                      item["accredited_university"], item["Alevel"], item["IB"], item["IELTS"],
                                      item["IELTS_L"], item["IELTS_S"], item["IELTS_R"], item["IELTS_W"], item["TOEFL"],
                                      item["TOEFL_L"], item["TOEFL_S"], item["TOEFL_R"], item["TOEFL_W"], item["GRE"],
                                      item["GMAT"], item["LSAT"], item["MCAT"], item["working_experience"],
                                      item["interview"], item["portfolio"], item["application_documents"],
                                      item["how_to_apply"], item["school_test"], item["SATI"], item["SATII"],
                                      item["SAT_code"], item["ACT"], item["ACT_code"], item["other"], item["url"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/"+item['university']+item['degree_level']+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n========================\n")
        # self.close()
        return item

