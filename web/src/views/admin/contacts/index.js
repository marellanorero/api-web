import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../../../store/appContext";
import { FaEdit, FaTrash } from 'react-icons/fa'

const ContactList = () => {
    const {store, actions: { setContact }} = useContext(Context)
    return(
        <table className="table">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Phone</th>
                <th scope="col" colSpan={2} width="10%">Actions</th>
                </tr>
            </thead>
            <tbody>
            {
                        !!store.contacts &&
                        store.contacts.map((contact) => {
                            return (
                <tr key={contact.id}>
                <th scope="row">{contact.id}</th>
                <td>{contact.name}</td>
                <td>{contact.email}</td>
                <td>{contact.phone}</td>
                <td><Link className="btn btn-info" to={"/admin/contact/"+contact.id+"/edit"} onClick={() => setContact(contact)}><FaEdit /></Link></td>
                <td><Link className="btn btn-danger"><FaTrash /></Link></td>
                </tr>
                        )})
            }
                
            </tbody>
            </table>
    )
}

export default ContactList;