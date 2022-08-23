import React from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import injectContext from "./store/appContext";

import Navbar from "./components/Navbar";

import Home from "./views/Home";
import ContactList from "./views/admin/contacts";
import EditContact from "./views/admin/contacts/edit";

const App = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Switch>
                <Route exact path="/admin/contact/:id/edit" component={EditContact} />
                <Route exact path="/admin/contacts" component={ContactList} />
                <Route exact path="/" component={Home} />
            </Switch>
        </BrowserRouter>
    )
}

export default injectContext(App);