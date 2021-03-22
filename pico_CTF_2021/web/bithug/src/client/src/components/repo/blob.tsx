import * as React from "react";

export interface Props {
    blob?: string;
}

export const Blob = (props: Props) => {
    return (
        <div className="bh-blob">
            { props.blob }
        </div>
    );
};
