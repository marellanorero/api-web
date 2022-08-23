import React, { useContext } from "react";
import { Context } from "../store/appContext";

const Home = () => {
    const { store } = useContext(Context);
    return (
        <div>
            <h1> Contacts List </h1>
            <div className="container">
                <div className="row">
                    {
                        !!store.contacts &&
                        store.contacts.map((contact) => {
                            return (
                                <div className="col-md-4" key={contact.id}>
                                    <div className="card" >
                                        <div className="card-header">
                                            {contact.name}
                                        </div>
                                        <ul className="list-group list-group-flush">
                                            <li className="list-group-item">{contact.email ? contact.email : "Sin email"}</li>
                                            <li className="list-group-item">{contact.phone}</li>
                                        </ul>
                                    </div>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default Home