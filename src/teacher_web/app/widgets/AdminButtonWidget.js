import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const AdminButtonWidget = ({buttonText, auth, to}) => {
    if(buttonText === undefined || buttonText === '' || auth === undefined || auth === false) {
        return (<Fragment></Fragment>);
    } else {
        
        let className = `navbar-brand btn btn-warning float-right`;

        return (
            <Link className={className} id="btn-new" to={to}>{buttonText}</Link>
        )
    }
};

export default AdminButtonWidget;