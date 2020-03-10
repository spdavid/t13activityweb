import { Activity, Member, PagedMembers } from "../Models";
import { useHistory } from "react-router-dom";
import React, { useContext, useState, useCallback } from "react";
import { userContext } from "./UserContext";
import { claimActivity } from "../logic/TaskActions";
import { Modal, Button } from "react-bootstrap";
import DataProvider from "./DataProvider";
import { deserialize } from "class-transformer";
import { MyProxiesTable } from "./ProxiesTable";

export const EnlistButtons = (props: {
    activity: Activity,
    reloadActivity: () => void
}) => {
    const { activity } = props;
    const history = useHistory();
    const user = useContext(userContext);
    const [showProxyDialog, setShowProxyDialog] = useState(false);

    const handleEnlistSelf = (e: React.MouseEvent<HTMLElement>) => {
        e.stopPropagation();
        claimActivity(props.activity, true, history);
    }

    const handleEnlistProxy = (e: React.MouseEvent<HTMLElement>) => {
        e.stopPropagation();
        setShowProxyDialog(true);
    }

    const handleHide = () => {
        setShowProxyDialog(false);
        props.reloadActivity();
    }

    if (activity.assigned?.id === user.memberId)
        return <Button variant='outline-danger' size='sm' href="/frontend/home?tab=my-tasks">Avboka</Button>

    var r = []

    if (!activity.event.current_user_assigned)
        r.push(<Button style={{ marginBottom: 3 }} onClick={handleEnlistSelf}>Boka</Button>)

    if (user.hasProxies)
        r.push(<>
            <ProxyDialog show={showProxyDialog} onHide={handleHide} activity={activity}/>
            <Button variant="outline-primary" onClick={handleEnlistProxy}>Boka underhuggare</Button>
        </>)

    return <>{r}</>;

}


const ProxyDialog = (props: { show: boolean, onHide: () => void, activity: Activity }) => {
    const [proxies, setProxies] = useState<Member[]>([]);
    const handleLoaded = useCallback((data: PagedMembers) => setProxies(data.results), [])

    return <Modal show={props.show} onHide={props.onHide}>
        <Modal.Header closeButton>
            <Modal.Title>Boka underhuggare</Modal.Title>
            <Modal.Body>
                <DataProvider<PagedMembers>
                    url={`/api/proxy/my`}
                    ctor={json => deserialize(PagedMembers, json)}
                    onLoaded={handleLoaded}>
                    <MyProxiesTable proxies={proxies}
                        activity={props.activity}
                        onEnlistChanged={() => window.location.reload()} />
                </DataProvider>
            </Modal.Body>
        </Modal.Header>
    </Modal>
}