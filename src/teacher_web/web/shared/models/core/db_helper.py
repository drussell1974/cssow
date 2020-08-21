# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""
import mysql.connector
from .log_type import LOG_TYPE

class TRANSACTION_STATE:
    NONE = None
    OPEN = 1
    DONE = 2


class ExecHelper:
    #############################
    # TODO: create as singleton #
    #############################

    db = None
    cur = None
    transaction_state = None

    def begin(self, db, transaction_state=TRANSACTION_STATE.NONE):
        """
        set start cursor (set autocommit to false if specified)

        :param db: the database context
        :param auto (default=True): whether to automatically commit or rollback
        """

        self.db = db
        if self.transaction_state is TRANSACTION_STATE.NONE:
            self.transaction_state = transaction_state
            #print("execHelper: begin {} transaction...".format(self.transaction_state))
            self.cur = self.db.cursor()
        
        if self.transaction_state == TRANSACTION_STATE.OPEN:
            #print("autocommit false...")
            self.db.autocommit = False


    def end_transaction(self):
        self.transaction_state = TRANSACTION_STATE.DONE


    def end(self):
        """ 
        close the cursor and connection if not set to automatically close
        """
        # only close if transaction is end_transaction has been called
        if self.transaction_state == TRANSACTION_STATE.NONE or self.transaction_state == TRANSACTION_STATE.DONE:
            #print("execHelper: closing...")
            self.cur.close()
            self.db.close()
            # reset
            self.transaction_state = TRANSACTION_STATE.NONE


    def commit(self):
        """
        Manually commit the transaction
        """
        # only call if end_transaction has been called
        if self.transaction_state == TRANSACTION_STATE.DONE:
            #print("execHelper: committing... {}".format(self.db.autocommit))
            self.db.commit()


    def rollback(self):
        """
        Manually rollback the transaction
        """
        #print("execHelper: rolling back... {}".format(self.transaction_state))
        
        if self.transaction_state == TRANSACTION_STATE.OPEN:
            self.db.rollback()
            #print("execHelper: rolled back!")
        
        # end_transaction has been called
        self.end_transaction()
        

    def select(self, db, sql, params, result, log_info=None):
    
        ''' run the sql statement '''
        self.begin(db)
    
        try:

            # DO THE WORK
            self.cur.callproc(sql, params)
            result = self.cur.fetchall()

            if log_info is not None:
                log_info(self.db, "update", "executed:{}, with results: fetchall returned = {}".format(sql, result), LOG_TYPE.Verbose)
            
            self.commit()

        except Exception as e:

            self.rollback()
            
            if log_info is not None:
                log_info(self.db, "ExecHelper.select", "An error occurred selecting data '%s'" % sql, log_type=LOG_TYPE.Error)    
            raise e
        finally:
            self.end()

        return result


    def scalar(self, db, sql, params, result, log_info=None):
        """ for sql queries returning a single value e.g row count """
        value = 1

        # TODO: implement callproc(sql, params)
        raise NotImplementedError("implement callproc(sql, params) to return a single value")

        return value
        

    def insert(self, db, sql, params, log_info=None):
        ''' run the sql statement '''

        result = []

        self.begin(db)

        try:

            # DO THE WORK
            
            self.cur.callproc(sql, params)                
            result = self.cur.fetchone()


            if log_info is not None:
                log_info(self.db, "update", "executed:{}, with results: new id = {}".format(sql, result), LOG_TYPE.Verbose)
            
            self.commit()

        except Exception as e:

            self.rollback()

            if log_info is not None:
                log_info(self.db, "ExecHelper.insert", "An error occurred inserting data '{}'".format(sql), LOG_TYPE.Error)    
            raise

        finally:
            self.end()

        return result


    def update(self, db, sql, params, log_info=None):
        ''' run the sql statement '''
        result = []

        self.begin(db)

        try:

            self.cur.callproc(sql, params)
            
            result = self.cur.rowcount
        
            if log_info is not None:
                log_info(self.db, "update", "executed:{}, with results: number of records affected = {}".format(sql, result), LOG_TYPE.Verbose)

            self.commit()

        except Exception as e:

            self.rollback()

            if log_info is not None:
                log_info(self.db, "ExecHelper.update", "An error occurred updating data '%s'" % sql, log_type=LOG_TYPE.Error)    
            raise e
        finally:
            self.end()

        return result


    def delete(self, db, sql, params, log_info=None):
        ''' run the sql statement '''

        result = []

        self.begin(db)

        try:

            self.cur.callproc(sql, params)
            
            result = self.cur.rowcount

            if log_info != None:
                log_info(self.db, "delete", "results: number of records affected = {}".format(result), LOG_TYPE.Verbose)
                
            if log_info is not None:
                log_info(self.db, "update", "executed:{}, with results: number of records affected = {}".format(sql, result), LOG_TYPE.Verbose)
            
            self.commit()
        
        except Exception as e:
        
            self.rollback()

            if log_info is not None:
                log_info(self.db, "ExecHelper.delete", "An error occurred deleting data '%s'" % sql, log_type=LOG_TYPE.Error)    
            raise e
        finally:
            self.end()

        return result


def to_empty(val):
    return "" if val is None else val


def sql_safe(string):
    return str(string).strip(' ')