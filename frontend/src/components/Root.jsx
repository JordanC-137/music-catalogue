import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";

export default function Root(){
    return (
        <>
            <Sidebar />
            <section className="main-component">
                <Outlet />
            </section>
        </>
    );
}