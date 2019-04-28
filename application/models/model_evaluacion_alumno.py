import web
import app 

db = app.db


def get_all_evaluacion_alumno():
    try:
        return db.select('evaluacion_alumno')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def alumno_evaluado(asesoria):
    try:
        results = db.query('SELECT COUNT(*) as total FROM evaluacion_alumno WHERE asesoria=$asesoria', vars=locals())
        for dato in results:
            return dato.total
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_reporte_asesor(num_as):
    try:
        return db.select('evaluacion_alumno', where='asesoria = $num_as', vars=locals())[0]
    except Exception as e:
        print "Model get_reporte_asesor Error {}".format(e.args)
        print "Model get_reporte_asesor Message {}".format(e.message)
        return None


def get_evaluacion_alumno(id_e):
    try:
        return db.select('evaluacion_alumno', where='id_e=$id_e', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_evaluacion_alumno(id_e):
    try:
        return db.delete('evaluacion_alumno', where='id_e=$id_e', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_evaluacion_alumno(asesoria,horas,asistencia,observaciones,calificacion,extra):
    try:
        return db.insert('evaluacion_alumno',
        asesoria=asesoria,
        horas=horas,
        asistencia=asistencia,
        observaciones=observaciones,
        calificacion=calificacion,
        extra=extra)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_evaluacion_alumno(id_e,asesoria,horas,asistencia,observaciones,calificacion,extra):
    try:
        return db.update('evaluacion_alumno',id_e=id_e,
asesoria=asesoria,
horas=horas,
asistencia=asistencia,
observaciones=observaciones,
calificacion=calificacion,
extra=extra,
                  where='id_e=$id_e',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
