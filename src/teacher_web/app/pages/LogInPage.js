import React, { Component } from 'react';
 
import LogInFormWidget from '../widgets/LogInFormWidget';

const LogInPageLayout = () => {
    return (
        <div className="col-lg-8 col-md-10 mx-auto">
            <LogInFormWidget auth={false} />
            <a id="register" href="/user/register">Register</a>
            <br />            
            <a id="reset" href="/user/retrieve_password">Lost your password?</a>                
       </div>
    )
}

class LogInPage extends Component {
    render() {
        return(
            <div className="col-lg-8 col-md-10 mx-auto">
                 <LogInPageLayout />
            </div>
        )
    }
}

export default LogInPage;